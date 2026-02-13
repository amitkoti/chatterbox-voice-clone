"""
Video Composer
Assembles slides, audio, and B-roll into final video
"""

import os
import glob
from pathlib import Path

try:
    # moviepy 2.x imports
    from moviepy import (
        VideoClip, ImageClip, AudioFileClip, concatenate_videoclips,
        CompositeVideoClip
    )
    import soundfile as sf
except ImportError as e:
    print(f"ERROR: Video dependencies not installed: {e}")
    print("Install with: pip install moviepy soundfile")
    print("Note: moviepy requires ffmpeg")
    raise

try:
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
except ImportError:
    print("ERROR: PIL not installed")
    print("Install with: pip install Pillow")
    raise


class VideoComposer:
    """Compose video from slides, audio, and B-roll"""

    def __init__(self, slides, audio_path, broll_dir=None,
                 resolution='1920x1080', fps=30, transition='fade',
                 project_dir='_projects/temp'):
        """
        Initialize composer

        Args:
            slides: List of slide data dicts from PowerPointParser
            audio_path: Path to narration audio file
            broll_dir: Directory containing B-roll footage
            resolution: Video resolution (e.g., '1920x1080')
            fps: Frames per second
            transition: Transition effect ('none', 'fade', 'slide', 'wipe')
            project_dir: Project directory for intermediate files
        """
        self.slides = slides
        self.audio_path = audio_path
        self.broll_dir = broll_dir
        self.fps = fps
        self.transition = transition
        self.project_dir = project_dir

        # Parse resolution
        w, h = resolution.lower().split('x')
        self.width = int(w)
        self.height = int(h)

        # Create slides directory
        self.slides_dir = f"{project_dir}/slides_rendered"
        os.makedirs(self.slides_dir, exist_ok=True)

    def create_video(self, output_file, pause_duration=0.5, min_slide_duration=3.0):
        """
        Create final video

        Args:
            output_file: Output video path
            pause_duration: Pause between slides (seconds)
            min_slide_duration: Minimum duration per slide (seconds)

        Returns:
            Path to created video
        """
        print(f"   Resolution: {self.width}x{self.height}")
        print(f"   FPS: {self.fps}")
        print(f"   Slides: {len(self.slides)}")

        # Step 1: Generate slide images
        print("\n   Generating slide images...")
        slide_images = self._generate_slide_images()

        # Step 2: Calculate timing
        print("   Calculating timing...")
        timings = self._calculate_timings(pause_duration, min_slide_duration)

        # Step 3: Create video clips
        print("   Creating video clips...")
        video_clips = self._create_video_clips(slide_images, timings)

        # Step 4: Concatenate clips
        print("   Combining clips...")
        final_video = concatenate_videoclips(video_clips, method='compose')

        # Step 5: Add audio if available
        if self.audio_path:
            print("   Adding audio...")
            final_video = self._add_audio(final_video)

        # Step 6: Write output
        print(f"   Writing video: {output_file}")
        final_video.write_videofile(
            output_file,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            preset='medium',
            ffmpeg_params=['-crf', '23']
        )

        # Cleanup
        final_video.close()

        return output_file

    def _generate_slide_images(self):
        """Generate images for each slide"""
        slide_images = []

        for i, slide in enumerate(self.slides, 1):
            image_path = f"{self.slides_dir}/slide_{i:03d}.png"

            # Create slide image
            self._create_slide_image(
                slide=slide,
                output_path=image_path,
                slide_number=i
            )

            slide_images.append(image_path)
            print(f"      [{i}/{len(self.slides)}] {slide['title'][:40]}...")

        return slide_images

    def _create_slide_image(self, slide, output_path, slide_number):
        """Create an image representation of a slide"""

        # Create blank slide
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Try to load fonts
        try:
            title_font = ImageFont.truetype("arial.ttf", 72)
            content_font = ImageFont.truetype("arial.ttf", 48)
            footer_font = ImageFont.truetype("arial.ttf", 32)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            footer_font = ImageFont.load_default()

        # Add colored header bar
        header_height = 150
        draw.rectangle(
            [(0, 0), (self.width, header_height)],
            fill='#2c3e50'
        )

        # Add title
        title = slide['title']
        title_y = 40

        # Word wrap title if too long
        if len(title) > 40:
            words = title.split()
            lines = []
            current_line = []
            for word in words:
                current_line.append(word)
                if len(' '.join(current_line)) > 40:
                    lines.append(' '.join(current_line[:-1]))
                    current_line = [word]
            if current_line:
                lines.append(' '.join(current_line))
            title = '\n'.join(lines[:2])  # Max 2 lines

        draw.text(
            (self.width // 2, title_y),
            title,
            fill='white',
            font=title_font,
            anchor='mt'
        )

        # Add content (bullet points)
        content = slide['content']
        if content and content != slide['title']:
            content_y = header_height + 100

            # Split into lines and limit
            content_lines = content.split('\n')[:5]  # Max 5 lines

            for line in content_lines:
                if line.strip():
                    # Add bullet point
                    bullet_text = f"• {line.strip()[:80]}"  # Truncate long lines

                    draw.text(
                        (100, content_y),
                        bullet_text,
                        fill='#2c3e50',
                        font=content_font
                    )
                    content_y += 80

        # Add slide number in footer
        footer_text = f"Slide {slide_number}"
        draw.text(
            (self.width - 100, self.height - 50),
            footer_text,
            fill='#95a5a6',
            font=footer_font,
            anchor='rm'
        )

        # Save image
        img.save(output_path)

    def _calculate_timings(self, pause_duration, min_slide_duration):
        """Calculate duration for each slide based on individual audio files"""

        timings = []

        for i, slide in enumerate(self.slides):
            # Check if this slide has its own audio file
            if 'audio_file' in slide and slide['audio_file']:
                try:
                    # Load this slide's audio to get its duration
                    audio_data, sample_rate = sf.read(slide['audio_file'])
                    slide_audio_duration = len(audio_data) / sample_rate

                    # Use actual audio duration + pause
                    duration = slide_audio_duration + pause_duration
                    timings.append(duration)
                    print(f"      Slide {i+1}: {slide_audio_duration:.1f}s audio + {pause_duration:.1f}s pause = {duration:.1f}s")

                except Exception as e:
                    print(f"      Warning: Could not load audio for slide {i+1}, using default: {e}")
                    timings.append(min_slide_duration + pause_duration)
            else:
                # No audio for this slide, use minimum duration
                timings.append(min_slide_duration + pause_duration)
                print(f"      Slide {i+1}: {min_slide_duration + pause_duration:.1f}s (no audio)")

        return timings

    def _create_video_clips(self, slide_images, timings):
        """Create video clips from slide images"""

        clips = []

        for i, (image_path, duration) in enumerate(zip(slide_images, timings)):
            # Create image clip
            clip = ImageClip(image_path).with_duration(duration)

            # Add transition effects (TODO: implement for moviepy 2.x)
            # if self.transition == 'fade' and i > 0:
            #     clip = clip.fadein(0.5)

            clips.append(clip)

        return clips

    def _add_audio(self, video_clip):
        """Add audio narration to video by concatenating per-slide audio"""

        # Collect audio clips from slides
        audio_clips = []
        for i, slide in enumerate(self.slides):
            if 'audio_file' in slide and slide['audio_file']:
                try:
                    audio_clip = AudioFileClip(slide['audio_file'])
                    audio_clips.append(audio_clip)
                except Exception as e:
                    print(f"      Warning: Could not load audio for slide {i+1}: {e}")

        if not audio_clips:
            print("      Warning: No audio files found, skipping audio")
            return video_clip

        try:
            # Concatenate all slide audio clips
            from moviepy import concatenate_audioclips
            combined_audio = concatenate_audioclips(audio_clips)

            # Adjust video duration to match audio if needed
            if combined_audio.duration > video_clip.duration:
                print(f"      Note: Audio longer than video ({combined_audio.duration:.1f}s vs {video_clip.duration:.1f}s)")

            # Set audio
            video_clip = video_clip.with_audio(combined_audio)

        except Exception as e:
            print(f"      Warning: Could not add audio: {e}")

        return video_clip


def test_composer():
    """Test the composer"""
    import sys

    print("=" * 70)
    print("Video Composer Test")
    print("=" * 70)

    # Create sample slides
    slides = [
        {
            'slide_number': 1,
            'title': 'Welcome to the Course',
            'content': 'Introduction\nOverview\nObjectives',
            'notes': 'Welcome everyone to this course.'
        },
        {
            'slide_number': 2,
            'title': 'Module Overview',
            'content': 'Topic 1\nTopic 2\nTopic 3',
            'notes': 'In this module we will cover three topics.'
        }
    ]

    composer = VideoComposer(
        slides=slides,
        audio_path=None,
        resolution='1920x1080',
        fps=30,
        project_dir='_projects/test'
    )

    output_file = '_projects/test/test_video.mp4'
    composer.create_video(output_file, min_slide_duration=5.0)

    print(f"\n✅ Test video created: {output_file}")


if __name__ == "__main__":
    test_composer()
