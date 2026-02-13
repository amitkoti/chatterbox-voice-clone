"""
Video Creator - Automated Video Generation from PowerPoint
Combines slides, voice narration, and B-roll into complete videos
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

# Add parent directory to path to import voice generation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    parser = argparse.ArgumentParser(
        description="Create videos from PowerPoint presentations with voice narration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic video from PowerPoint
  python video_creator.py presentation.pptx

  # Generate audio files only (run on any idle system)
  python video_creator.py slides.pptx --audio-only

  # Create video using pre-generated audio (fast!)
  python video_creator.py slides.pptx --use-existing-audio

  # Specify voice and output
  python video_creator.py slides.pptx --voice amit --output video.mp4

  # Include B-roll footage
  python video_creator.py slides.pptx --broll demos/ --captions

  # Quick preview (first 3 slides only)
  python video_creator.py slides.pptx --preview 3
        """
    )

    # Required arguments
    parser.add_argument('presentation',
                       help='PowerPoint file (.pptx)')

    # Voice options
    parser.add_argument('--voice', '-v',
                       choices=['amit', 'a', 'saanvi', 's'],
                       default='amit',
                       help='Voice to use (default: amit)')

    # Output options
    parser.add_argument('--output', '-o',
                       help='Output video file (default: auto-generated)')

    parser.add_argument('--resolution',
                       default='1920x1080',
                       help='Video resolution (default: 1920x1080)')

    parser.add_argument('--fps',
                       type=int,
                       default=30,
                       help='Frames per second (default: 30)')

    # B-roll options
    parser.add_argument('--broll', '-b',
                       help='Directory containing B-roll footage')

    # Timing options
    parser.add_argument('--pause',
                       type=float,
                       default=0.5,
                       help='Pause between slides in seconds (default: 0.5)')

    parser.add_argument('--min-duration',
                       type=float,
                       default=3.0,
                       help='Minimum slide duration in seconds (default: 3.0)')

    # Features
    parser.add_argument('--captions', '-c',
                       action='store_true',
                       help='Generate captions/subtitles')

    parser.add_argument('--chapters',
                       action='store_true',
                       help='Add chapter markers')

    parser.add_argument('--preview', '-p',
                       type=int,
                       metavar='N',
                       help='Preview mode: generate only first N slides')

    # Transition effects
    parser.add_argument('--transition',
                       choices=['none', 'fade', 'slide', 'wipe'],
                       default='fade',
                       help='Transition effect between slides (default: fade)')

    # Advanced options
    parser.add_argument('--audio-only',
                       action='store_true',
                       help='Generate audio files only, skip video creation')

    parser.add_argument('--use-existing-audio',
                       action='store_true',
                       help='Use existing audio files, skip audio generation')

    parser.add_argument('--project-dir',
                       help='Project directory for outputs (default: _projects/[name])')

    args = parser.parse_args()

    # Validate presentation file
    if not os.path.exists(args.presentation):
        print(f"ERROR: Presentation file not found: {args.presentation}")
        return 1

    print("=" * 70)
    print("VIDEO CREATOR - Automated Video Generation")
    print("=" * 70)
    print()

    # Import required modules
    try:
        from ppt_parser import PowerPointParser
        from video_composer import VideoComposer
    except ImportError as e:
        print(f"ERROR: Missing required modules: {e}")
        print("\nPlease install video dependencies:")
        print("  pip install -r requirements_video.txt")
        return 1

    # Determine voice reference
    if args.voice in ['amit', 'a']:
        voice_ref = "_reference_audio/audio_sample.wav"
        voice_name = "Amit"
    else:
        voice_ref = "_reference_audio/Saanvi_Voice_Clone.wav"
        voice_name = "Saanvi"

    # Check voice reference exists
    if not os.path.exists(voice_ref):
        print(f"ERROR: Voice reference not found: {voice_ref}")
        return 1

    # Setup project directory
    pres_name = Path(args.presentation).stem
    if args.project_dir:
        project_dir = args.project_dir
    else:
        project_dir = f"_projects/{pres_name}"

    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(f"{project_dir}/output", exist_ok=True)

    print(f"Project: {project_dir}")
    print(f"Voice: {voice_name}")
    print(f"Resolution: {args.resolution}")
    print(f"FPS: {args.fps}")
    print(f"Transition: {args.transition}")
    if args.preview:
        print(f"Preview Mode: First {args.preview} slides only")
    print()

    # Step 1: Parse PowerPoint
    print("Step 1: Parsing PowerPoint presentation...")
    print("-" * 70)

    try:
        parser_obj = PowerPointParser(args.presentation)
        slides = parser_obj.parse(preview_count=args.preview)

        print(f"Found {len(slides)} slides")
        for i, slide in enumerate(slides, 1):
            print(f"   {i}. {slide['title'][:50]}...")
        print()

    except Exception as e:
        print(f"ERROR parsing PowerPoint: {e}")
        return 1

    # Step 2: Generate or load voice narration (per-slide for perfect sync)
    if args.use_existing_audio:
        print("Step 2: Loading existing audio files...")
        print("-" * 70)

        import glob
        slide_audio_files = []
        found_count = 0

        for i, slide in enumerate(slides, 1):
            # Look for existing audio file for this slide
            slide_audio_pattern = f"{project_dir}/output/slide_{i:02d}_audio_*_complete.wav"
            audio_files = glob.glob(slide_audio_pattern)

            if audio_files:
                slide_audio_files.append(audio_files[0])
                found_count += 1
                print(f"   [{i}/{len(slides)}] Found: {os.path.basename(audio_files[0])}")
            else:
                slide_audio_files.append(None)
                print(f"   [{i}/{len(slides)}] Missing audio file")

        # Store audio files in slides data
        for i, slide in enumerate(slides):
            slide['audio_file'] = slide_audio_files[i] if i < len(slide_audio_files) else None

        print(f"\n   Loaded {found_count}/{len(slides)} audio files")

        if found_count == 0:
            print("\nWARNING: No audio files found!")
            print("Expected files like: slide_01_audio_*_complete.wav")
            print(f"In directory: {project_dir}/output/")
            return 1

    else:
        print("Step 2: Generating voice narration...")
        print("-" * 70)

        try:
            # Import voice generation
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_scripts'))
            from generate_long_audio import generate_long_audio, split_into_sentences

            # Generate separate audio for each slide
            slide_audio_files = []
            for i, slide in enumerate(slides, 1):
                if slide['notes']:
                    print(f"   [{i}/{len(slides)}] {slide['notes'][:60]}...")

                    # Generate audio for this specific slide
                    slide_audio_name = f"{project_dir}/output/slide_{i:02d}_audio"
                    generate_long_audio(
                        text=slide['notes'],
                        voice_reference=voice_ref,
                        output_name=slide_audio_name,
                        save_parts=False  # Don't need parts for individual slides
                    )

                    # Find the generated audio file
                    import glob
                    audio_files = glob.glob(f"{slide_audio_name}_*_complete.wav")
                    if audio_files:
                        slide_audio_files.append(audio_files[0])
                    else:
                        slide_audio_files.append(None)
                else:
                    print(f"   [{i}/{len(slides)}] (no notes)")
                    slide_audio_files.append(None)

            # Store audio files in slides data for VideoComposer
            for i, slide in enumerate(slides):
                slide['audio_file'] = slide_audio_files[i] if i < len(slide_audio_files) else None

            print(f"\n   Generated {len([f for f in slide_audio_files if f])} audio files")

        except Exception as e:
            print(f"ERROR generating audio: {e}")
            import traceback
            traceback.print_exc()
            return 1

    print()

    # If audio-only mode, exit here
    if args.audio_only:
        print("=" * 70)
        print("AUDIO GENERATION COMPLETE!")
        print("=" * 70)
        print(f"\nProject directory: {project_dir}/")
        print(f"Audio files: {project_dir}/output/slide_*_audio_*_complete.wav")
        print(f"\nGenerated {len([s for s in slides if s.get('audio_file')])} audio files")
        print("\nNext steps:")
        print(f"   To create video: python video_creator.py {args.presentation} --use-existing-audio")
        return 0

    # Step 3: Create video
    print("Step 3: Creating video...")
    print("-" * 70)

    try:
        composer = VideoComposer(
            slides=slides,
            audio_path=None,  # Audio files now in slide data
            broll_dir=args.broll,
            resolution=args.resolution,
            fps=args.fps,
            transition=args.transition,
            project_dir=project_dir
        )

        # Determine output filename
        if args.output:
            output_file = args.output
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"{project_dir}/output/{pres_name}_{timestamp}.mp4"

        print(f"   Creating: {output_file}")

        # Compose video
        video_path = composer.create_video(
            output_file=output_file,
            pause_duration=args.pause,
            min_slide_duration=args.min_duration
        )

        print(f"Video created: {video_path}")

    except Exception as e:
        print(f"ERROR creating video: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # Step 4: Generate captions (if requested)
    if args.captions:
        print("\nStep 4: Generating captions...")
        print("-" * 70)
        print("   (Caption generation coming soon)")

    # Step 5: Generate chapter markers (if requested)
    if args.chapters:
        print("\nStep 5: Generating chapter markers...")
        print("-" * 70)

        timestamps_file = f"{project_dir}/output/{pres_name}_timestamps.txt"
        with open(timestamps_file, 'w', encoding='utf-8') as f:
            f.write(f"YouTube Chapter Markers for: {pres_name}\n")
            f.write("=" * 70 + "\n\n")

            current_time = 0
            for i, slide in enumerate(slides, 1):
                mins = int(current_time // 60)
                secs = int(current_time % 60)
                f.write(f"{mins:02d}:{secs:02d} - {slide['title']}\n")

                # Estimate duration (will be refined with actual audio)
                current_time += args.min_duration + args.pause

        print(f"Chapter markers: {timestamps_file}")

    # Final summary
    print("\n" + "=" * 70)
    print("SUCCESS! Video generation complete!")
    print("=" * 70)
    print(f"\nProject directory: {project_dir}/")
    print(f"Video file: {video_path}")
    print(f"Audio files: {project_dir}/output/slide_*_audio_*_complete.wav")
    if args.chapters:
        print(f"Timestamps: {timestamps_file}")

    print("\nNext steps:")
    print(f"   1. Review: {video_path}")
    print(f"   2. Edit if needed")
    print(f"   3. Upload to YouTube!")

    if not args.use_existing_audio:
        print("\nTip: Audio files are saved! To recreate video faster:")
        print(f"   python video_creator.py {args.presentation} --use-existing-audio")

    return 0

if __name__ == "__main__":
    sys.exit(main())
