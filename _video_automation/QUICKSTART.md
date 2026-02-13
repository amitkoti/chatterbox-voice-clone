# Video Automation - Quick Start Guide

Get started creating videos in 5 minutes!

---

## Step 1: Install Dependencies (One-Time Setup)

```bash
# Install video creation libraries
pip install -r _video_automation/requirements_video.txt

# Install ffmpeg (required for video encoding)
winget install ffmpeg
```

---

## Step 2: Create Your PowerPoint

### Simple Example

**Slide 1 - Title:**
- Title: "Welcome to My Course"
- Speaker Notes: "Hello everyone, welcome to this tutorial."

**Slide 2 - Main Content:**
- Title: "Key Concepts"
- Content: Bullet points
- Speaker Notes: "Today we'll cover three important concepts. First is variables, second is functions, and third is classes."

**Slide 3 - Thank You:**
- Title: "Thank You"
- Speaker Notes: "Thanks for watching! See you in the next video."

### Save As: `my_tutorial.pptx`

---

## Step 3: Generate Video

```bash
# Basic - generates video with Amit's voice
python _video_automation/video_creator.py my_tutorial.pptx

# With options
python _video_automation/video_creator.py my_tutorial.pptx --captions --chapters
```

---

## Step 4: Find Your Video

Look in: `_projects/my_tutorial/output/my_tutorial_TIMESTAMP.mp4`

---

## That's It! 🎉

Your video is ready to upload to YouTube!

---

## Next Steps

### Test First (Recommended)
```bash
# Generate only first 3 slides to test
python _video_automation/video_creator.py my_tutorial.pptx --preview 3
```

### Add Screen Recordings

1. Put demo videos in `_broll/screen_recordings/`
2. In PowerPoint speaker notes, add: `[SCREEN:demo.mp4]`
3. Generate video - B-roll automatically included!

### Use Different Voice
```bash
# Use Saanvi's voice instead
python _video_automation/video_creator.py my_tutorial.pptx --voice saanvi
```

---

## Common Commands

```bash
# Basic video
python _video_automation/video_creator.py slides.pptx

# With captions and chapters
python _video_automation/video_creator.py slides.pptx --captions --chapters

# Preview first 5 slides
python _video_automation/video_creator.py slides.pptx --preview 5

# Custom output location
python _video_automation/video_creator.py slides.pptx --output my_video.mp4

# Include screen recordings
python _video_automation/video_creator.py slides.pptx --broll _broll/screen_recordings/
```

---

## Tips

1. **Write speaker notes for every slide** - That's what gets narrated
2. **Keep slides simple** - Less text = better videos
3. **Use --preview first** - Test before generating full video
4. **Add pauses** - Use `[PAUSE:2]` in notes for 2-second pause
5. **Organize B-roll** - Keep recordings in `_broll/screen_recordings/`

---

## Need Help?

- Full documentation: `README_VIDEO.md`
- Main voice cloning: `../README.md`
- Examples: `examples/` folder

---

**Ready to create amazing videos? Start now! 🚀**
