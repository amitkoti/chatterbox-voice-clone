# Video Automation System

Automatically create professional videos from PowerPoint presentations with AI voice narration.

---

## 🎬 What This Does

Converts your PowerPoint slides + speaker notes into complete videos with:
- ✅ AI voice narration (Amit or Saanvi)
- ✅ Professional slide transitions
- ✅ Screen recording integration (B-roll)
- ✅ Automatic timing synchronization
- ✅ Optional captions and chapter markers

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install video creation libraries
pip install -r _video_automation/requirements_video.txt

# Install ffmpeg (required for video encoding)
# Windows:
winget install ffmpeg
# Or download from: https://ffmpeg.org/download.html
```

### 2. Prepare Your PowerPoint

Create a PowerPoint with:
- Slides (your visual content)
- **Speaker Notes** (what to narrate for each slide)

**Example Speaker Notes:**
```
Welcome to Module 2 of our course on AI fundamentals.
In this video, we'll explore three key concepts.
[PAUSE:2] Let me show you a demonstration.
[SCREEN:demo.mp4]
```

### 3. Generate Video

```bash
# Basic usage
python _video_automation/video_creator.py presentation.pptx

# With options
python _video_automation/video_creator.py presentation.pptx \
    --voice amit \
    --captions \
    --chapters \
    --output my_video.mp4
```

---

## 📖 Usage Guide

### Basic Command

```bash
python _video_automation/video_creator.py <presentation.pptx>
```

### Common Options

```bash
# Choose voice
--voice amit        # Use Amit's voice (default)
--voice saanvi      # Use Saanvi's voice

# Output options
--output video.mp4  # Specify output filename
--resolution 1920x1080  # Video resolution (default)
--fps 30            # Frames per second

# Features
--captions          # Generate subtitles
--chapters          # Create YouTube chapter markers
--preview 3         # Generate only first 3 slides (for testing)

# Timing
--pause 0.5         # Pause between slides (seconds)
--min-duration 3.0  # Minimum slide duration (seconds)

# B-roll
--broll demos/      # Directory with screen recordings
```

### Complete Example

```bash
python _video_automation/video_creator.py \
    module_02_slides.pptx \
    --voice amit \
    --broll _broll/screen_recordings/ \
    --captions \
    --chapters \
    --pause 1.0 \
    --output _projects/module_02/output/module_02_final.mp4
```

---

## 📁 Project Structure

When you run the video creator, it creates:

```
_projects/
└── your_presentation/
    ├── slides_rendered/          # Generated slide images
    │   ├── slide_001.png
    │   ├── slide_002.png
    │   └── ...
    ├── output/
    │   ├── your_presentation_narration.wav  # Generated audio
    │   ├── your_presentation_20240211_143022.mp4  # Final video
    │   └── your_presentation_timestamps.txt  # Chapter markers
    └── demos/                    # B-roll footage (if any)
```

---

## 🎤 PowerPoint Speaker Notes

### Basic Narration

Just write what you want to say:

```
Welcome to this tutorial on Python programming.
Today we'll learn about functions and how to use them effectively.
```

### Special Markers

Add these to your speaker notes for advanced features:

#### Screen Recording / B-roll

```
Let me show you how this works in practice.
[SCREEN:demo1.mp4]
As you can see, the function returns the result.
```

The video will:
1. Show your slide
2. Switch to `demo1.mp4` screen recording
3. Return to slides
4. Continue narration

#### Pauses

```
There are three main concepts. [PAUSE:2]
First is variables. [PAUSE:1.5]
Second is functions.
```

Adds silence between sentences (in seconds).

#### Speed Control

```
[SLOW] This is a complex concept, so I'll explain slowly.
[FAST] Now let's quickly review what we learned.
[SPEED:0.8] Custom speed factor (0.8 = 20% slower).
```

---

## 🎯 Complete Workflow Example

### Step 1: Create PowerPoint

**Slide 1: Title**
- Title: "Introduction to Machine Learning"
- Speaker Notes: "Welcome to this course on machine learning. I'm excited to guide you through these concepts."

**Slide 2: Overview**
- Title: "What We'll Cover"
- Content: Bullet points with topics
- Speaker Notes: "In this module, we'll explore three key areas. [PAUSE:1] First is supervised learning, second is unsupervised learning, and third is reinforcement learning."

**Slide 3: Demo**
- Title: "Live Demonstration"
- Speaker Notes: "Let me show you how this works in practice. [SCREEN:ml_demo.mp4] As you can see, the model learns from the data."

### Step 2: Prepare B-roll

Place screen recordings in `_broll/screen_recordings/`:
```
_broll/screen_recordings/ml_demo.mp4
```

### Step 3: Generate Video

```bash
python _video_automation/video_creator.py \
    ml_course.pptx \
    --voice amit \
    --broll _broll/screen_recordings/ \
    --captions \
    --chapters \
    --output ml_module_01.mp4
```

### Step 4: Review & Upload

1. Review generated video: `_projects/ml_course/output/ml_module_01.mp4`
2. Check chapter markers: `_projects/ml_course/output/ml_course_timestamps.txt`
3. Upload to YouTube with chapters in description

---

## 🎨 Customization

### Slide Templates

Edit `video_composer.py` to customize slide appearance:
- Colors
- Fonts
- Layout
- Animations

### Transitions

Choose transition effects:
```bash
--transition fade   # Fade in/out (default)
--transition slide  # Slide transition
--transition wipe   # Wipe effect
--transition none   # No transition
```

### Voice Selection

Switch between voices:
```bash
--voice amit     # Professional narration
--voice saanvi   # Friendly, engaging tone
```

---

## 💡 Tips & Best Practices

### PowerPoint Tips

1. **Keep slides simple** - Less text = easier to read
2. **Use speaker notes** - Write complete narration scripts
3. **One idea per slide** - Better pacing and comprehension
4. **Consistent formatting** - Professional appearance

### Narration Tips

1. **Write naturally** - Speak conversationally in notes
2. **Use pauses** - Add [PAUSE:1] for emphasis
3. **Test audio first** - Use `amit_narrate.py` to preview
4. **Mark B-roll clearly** - Use [SCREEN:file] markers

### Video Production Tips

1. **Preview first** - Use `--preview 3` to test
2. **Check timing** - Ensure slides match narration
3. **Test B-roll** - Verify screen recordings work
4. **Generate chapters** - Always use `--chapters` for YouTube

---

## 🔧 Troubleshooting

### "ffmpeg not found"

Install ffmpeg:
```bash
# Windows
winget install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

### "Audio longer than video"

- Add more slides
- Reduce narration length
- Increase `--min-duration`

### "No speaker notes found"

- Ensure PowerPoint has speaker notes
- Check notes appear in PowerPoint's Notes pane
- Notes must be non-empty

### "B-roll file not found"

- Check file path in [SCREEN:filename]
- Verify file exists in `--broll` directory
- Use relative paths from broll directory

### "Video creation failed"

- Check all dependencies installed
- Verify ffmpeg is accessible
- Check disk space for output
- Review error messages for specifics

---

## 📊 Performance

### Generation Time

| Duration | Slides | Narration | Video Creation | Total |
|----------|--------|-----------|----------------|-------|
| 5 min    | 10     | ~5 min    | ~2 min         | ~7 min |
| 10 min   | 20     | ~10 min   | ~4 min         | ~14 min |
| 20 min   | 40     | ~20 min   | ~8 min         | ~28 min |

**Note:** With GPU, narration time reduces by 5-10x!

### File Sizes

| Resolution | 5 min video | 10 min video | 20 min video |
|------------|-------------|--------------|--------------|
| 1920x1080  | ~50 MB      | ~100 MB      | ~200 MB      |
| 1280x720   | ~25 MB      | ~50 MB       | ~100 MB      |

---

## 🚀 Advanced Features (Coming Soon)

- [ ] Automatic bullet point animations
- [ ] Picture-in-picture webcam overlay
- [ ] Multi-voice dialogue (Amit + Saanvi)
- [ ] Background music mixing
- [ ] Auto-generated captions (SRT)
- [ ] Template system for slide designs
- [ ] Batch processing (multiple presentations)
- [ ] Resume interrupted generation

---

## 📚 Examples

### Example 1: Simple Course Video

```bash
python _video_automation/video_creator.py course.pptx --voice amit
```

### Example 2: Tutorial with Demos

```bash
python _video_automation/video_creator.py tutorial.pptx \
    --voice amit \
    --broll demos/ \
    --chapters
```

### Example 3: Quick Preview

```bash
python _video_automation/video_creator.py presentation.pptx \
    --preview 5 \
    --output preview.mp4
```

### Example 4: Full Production

```bash
python _video_automation/video_creator.py \
    full_course.pptx \
    --voice amit \
    --broll _broll/screen_recordings/ \
    --captions \
    --chapters \
    --resolution 1920x1080 \
    --fps 30 \
    --pause 1.0 \
    --transition fade \
    --output final_video.mp4
```

---

## 🎓 Learning Path

1. **Start Simple**: Create basic video from PowerPoint
2. **Add Narration**: Write speaker notes for all slides
3. **Add B-roll**: Include screen recordings
4. **Polish**: Add chapters, captions, transitions
5. **Optimize**: Adjust timing, pacing, effects

---

## 💬 Need Help?

- Check main README: `../README.md`
- Review examples in `examples/`
- Test with `--preview` mode first
- Read error messages carefully

---

**Last Updated:** February 11, 2026
**Status:** Beta - Core features working, advanced features in development

Happy video creating! 🎬🚀
