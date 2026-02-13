# Video Creation Workflow Guide

## Overview

The video creator now supports **separate audio generation** and **video creation** steps. This allows you to:
- Generate audio files on any available system
- Create videos quickly using pre-generated audio
- Regenerate videos without waiting 20+ minutes for audio

---

## Workflow Options

### Option 1: Traditional (All-in-One)
Generate audio and video in one command:
```bash
python video_creator.py presentation.pptx
```
**Time**: ~20-25 minutes (audio generation + video creation)

---

### Option 2: Separate Audio Generation (RECOMMENDED)

#### Step 1: Generate Audio (Run on ANY idle system)
```bash
python video_creator.py presentation.pptx --audio-only
```
**Output**: `_projects/presentation/output/slide_XX_audio_*_complete.wav`
**Time**: ~20 minutes (but can run on any idle system!)

#### Step 2: Create Video (Run on ANY system, FAST!)
```bash
python video_creator.py presentation.pptx --use-existing-audio
```
**Time**: ~30 seconds to 2 minutes (just video composition)

---

## Multi-System Setup

### Scenario: You have 5 idle systems (A, B, C, D, E)

#### Generate Audio for Multiple Presentations in Parallel

**System A:**
```bash
python video_creator.py presentation1.pptx --audio-only --voice amit
```

**System B:**
```bash
python video_creator.py presentation2.pptx --audio-only --voice saanvi
```

**System C:**
```bash
python video_creator.py presentation3.pptx --audio-only --voice amit
```

**System D:**
```bash
python video_creator.py presentation4.pptx --audio-only --voice amit
```

**System E:**
```bash
python video_creator.py presentation5.pptx --audio-only --voice saanvi
```

#### Create Videos Later (on ANY system)

Once audio is generated, create videos quickly:
```bash
# Create all videos at once (fast!)
python video_creator.py presentation1.pptx --use-existing-audio
python video_creator.py presentation2.pptx --use-existing-audio
python video_creator.py presentation3.pptx --use-existing-audio
python video_creator.py presentation4.pptx --use-existing-audio
python video_creator.py presentation5.pptx --use-existing-audio
```

---

## Benefits

### 1. **Faster Iteration**
Regenerate videos with different settings without re-generating audio:
```bash
# Try different transitions
python video_creator.py slides.pptx --use-existing-audio --transition fade
python video_creator.py slides.pptx --use-existing-audio --transition slide

# Adjust timing
python video_creator.py slides.pptx --use-existing-audio --pause 1.0 --min-duration 5.0
```

### 2. **Parallel Processing**
- Generate audio for 5 presentations simultaneously on 5 systems
- Each takes ~20 minutes, but all finish at the same time
- Total time: 20 minutes instead of 100 minutes!

### 3. **Resource Optimization**
- Audio generation: CPU-intensive (use idle systems)
- Video creation: Fast (can run on main system)

### 4. **Flexibility**
- Generate audio at night on idle systems
- Create videos the next day
- Reuse audio for multiple video versions

---

## File Structure

When you run `--audio-only`, files are saved in the project directory:

```
_projects/
└── presentation_name/
    └── output/
        ├── slide_01_audio_20260212_143022_complete.wav
        ├── slide_02_audio_20260212_143045_complete.wav
        ├── slide_03_audio_20260212_143108_complete.wav
        └── ...
```

These audio files are **automatically detected** when you run `--use-existing-audio`.

---

## Tips

### Verify Audio Files
After generating audio, check that all files were created:
```bash
# Windows
dir _projects\presentation_name\output\slide_*_audio_*.wav

# Linux/Mac
ls _projects/presentation_name/output/slide_*_audio_*.wav
```

### Preview Mode with Pre-generated Audio
Test video creation with just the first 3 slides:
```bash
python video_creator.py slides.pptx --preview 3 --audio-only
python video_creator.py slides.pptx --preview 3 --use-existing-audio
```

### Share Audio Files Across Systems
If using network shared folder or manual file transfer:
1. Generate audio on System A
2. Copy `_projects/presentation_name/` folder to System B
3. Create video on System B using `--use-existing-audio`

---

## Troubleshooting

### "Missing audio file" errors
**Problem**: Audio files not found when using `--use-existing-audio`

**Solution**:
1. Check the project directory exists: `_projects/[presentation_name]/output/`
2. Verify audio files exist with pattern: `slide_XX_audio_*_complete.wav`
3. Run `--audio-only` first to generate missing files

### Audio-video sync issues
**Problem**: Slides transition at wrong times

**Solution**: This should NOT happen with per-slide audio! If it does:
1. Check that audio files were generated properly
2. Verify each slide has corresponding audio file
3. Report the issue - this indicates a bug

---

## Quick Reference

| Command | Purpose | Time | Use Case |
|---------|---------|------|----------|
| `--audio-only` | Generate audio files only | ~20 min | Run on idle systems |
| `--use-existing-audio` | Create video from existing audio | ~1-2 min | Fast video creation |
| `[no flags]` | Generate audio + video | ~20-25 min | All-in-one workflow |
| `--preview N` | Only process first N slides | Varies | Quick testing |
| `--voice amit/saanvi` | Choose voice | N/A | Different voices |

---

## Best Practices

1. **Generate audio first** on idle systems overnight
2. **Create videos next day** quickly with `--use-existing-audio`
3. **Keep audio files** - they're your time investment!
4. **Use preview mode** (`--preview 3`) to test before full generation
5. **Parallel processing** - utilize all 5 idle systems simultaneously

---

## Example: Full Production Workflow

```bash
# Night time: Generate audio on 5 systems in parallel
# System A, B, C, D, E - each processing different presentations
python video_creator.py presentation1.pptx --audio-only --voice amit    # 20 min
python video_creator.py presentation2.pptx --audio-only --voice amit    # 20 min
python video_creator.py presentation3.pptx --audio-only --voice saanvi  # 20 min
python video_creator.py presentation4.pptx --audio-only --voice amit    # 20 min
python video_creator.py presentation5.pptx --audio-only --voice saanvi  # 20 min

# Next day: Create all videos quickly (total ~10 minutes)
python video_creator.py presentation1.pptx --use-existing-audio  # 2 min
python video_creator.py presentation2.pptx --use-existing-audio  # 2 min
python video_creator.py presentation3.pptx --use-existing-audio  # 2 min
python video_creator.py presentation4.pptx --use-existing-audio  # 2 min
python video_creator.py presentation5.pptx --use-existing-audio  # 2 min

# Total wall-clock time: 20 min (overnight) + 10 min (next day) = 30 min
# vs. Sequential: 100 min (audio) + 10 min (video) = 110 min
# Speedup: 3.7x faster!
```
