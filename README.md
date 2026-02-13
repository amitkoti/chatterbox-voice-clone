# Voice Cloning System - Chatterbox TTS

Complete voice cloning system using Chatterbox TTS with support for multiple voices.

**🎬 NEW: Video Automation System** - Create complete videos from PowerPoint + voice narration! See `_video_automation/` folder.

---

## ✅ Yes, You Can Run From PowerShell!

All Python scripts can be run directly from PowerShell:
```powershell
python amit_narrate.py your_script.txt
python clone_amit_voice.py
python clone_saanvi_voice.py
```

---

## 📁 Folder Structure

```
Chartterbox/
│
├── README.md                       # This file
│
├── _reference_audio/               # Voice samples (DO NOT DELETE)
│   ├── audio_sample.wav           # Amit's voice reference
│   └── Saanvi_Voice_Clone.wav     # Saanvi's voice reference
│
├── Main Scripts (USE THESE):
│   ├── amit_narrate.py            # Generate audio with Amit's voice (from file)
│   ├── clone_amit_voice.py        # Generate audio with Amit's voice (paste in script)
│   └── clone_saanvi_voice.py      # Generate audio with Saanvi's voice
│
├── _scripts/                       # Utility scripts
│   ├── combine_audio_files.py     # Combine multiple audio files
│   └── generate_long_audio.py     # Universal long audio generator
│
├── _video_automation/              # 🎬 NEW - Video Creation System
│   ├── video_creator.py            # Main video automation tool
│   ├── ppt_parser.py               # PowerPoint reader
│   ├── video_composer.py           # Video assembler
│   ├── README_VIDEO.md             # Video automation guide
│   └── requirements_video.txt      # Video dependencies
│
├── _projects/                      # Video projects (auto-created)
│   └── [your_videos]/              # Individual video projects
│
├── _broll/                         # B-roll footage library
│   ├── screen_recordings/          # Screen demos
│   ├── intro_outros/               # Intro/outro clips
│   └── transitions/                # Transition effects
│
├── _docs/                          # Documentation
│   ├── VOICE_CLONES_QUICK_REFERENCE.md
│   ├── AUDIO_LENGTH_GUIDE.md
│   └── VOICE_CLONING_GUIDE.md
│
├── Output Folders:
│   ├── Amit_Clone/                # Amit's generated audio files
│   └── Saanvi_Clone/              # Saanvi's generated audio files
│
└── _archive/                       # Old/test files (safe to delete)
```

---

## 🎯 Required Files (DO NOT DELETE)

### Essential Files:
1. **_reference_audio/audio_sample.wav** - Amit's voice sample
2. **_reference_audio/Saanvi_Voice_Clone.wav** - Saanvi's voice sample
3. **amit_narrate.py** - Main script for Amit's voice
4. **clone_amit_voice.py** - Alternative Amit script
5. **clone_saanvi_voice.py** - Main script for Saanvi's voice

### Your Script:
- **module_02_video_script.md** - Your video script (currently being generated)

### Can Be Deleted:
- **_archive/** folder - Contains old test files and outputs
- Individual **cloned_output_*.wav** files (moved to _archive)

---

## 🚀 How To Use

### Option 1: Generate Amit's Voice from Text File (Recommended)

1. **Create a text file** with your script:
   ```powershell
   # Create file in Notepad
   notepad my_script.txt
   ```

2. **Run the generation:**
   ```powershell
   python amit_narrate.py my_script.txt
   ```

3. **Find output in:**
   ```
   Amit_Clone/amit_TIMESTAMP.wav
   ```

### Option 2: Paste Script Directly

1. **Edit the script file:**
   ```powershell
   notepad clone_amit_voice.py
   ```

2. **Find this section and paste your text:**
   ```python
   YOUR_SCRIPT = """
   Paste your text here
   """
   ```

3. **Run:**
   ```powershell
   python clone_amit_voice.py
   ```

### Option 3: Generate Saanvi's Voice

1. **Edit the script:**
   ```powershell
   notepad clone_saanvi_voice.py
   ```

2. **Modify the test_sentences list**

3. **Run:**
   ```powershell
   python clone_saanvi_voice.py
   ```

---

## 🎬 NEW: Video Automation (PowerPoint → Video)

### Create Complete Videos from Presentations!

Turn your PowerPoint slides + speaker notes into professional videos automatically!

**Quick Start:**
```powershell
# Install video dependencies
pip install -r _video_automation/requirements_video.txt

# Create video from PowerPoint
python _video_automation/video_creator.py your_slides.pptx
```

**What It Does:**
1. ✅ Reads PowerPoint slides
2. ✅ Generates voice narration from speaker notes
3. ✅ Creates video with slide transitions
4. ✅ Syncs audio with slides
5. ✅ Adds B-roll/screen recordings
6. ✅ Exports YouTube-ready video

**Features:**
- 🎤 AI voice narration (Amit or Saanvi)
- 📊 Professional slide rendering
- 🎬 Automatic timing synchronization
- 📹 Screen recording integration
- 📝 Chapter markers for YouTube
- 🎞️ Multiple transition effects

**Example PowerPoint Setup:**

```
Slide 1: Introduction
Speaker Notes: "Welcome to Module 2. In this video, we'll explore three key concepts."

Slide 2: Core Concept
Speaker Notes: "The first concept is important. [PAUSE:2] Let me demonstrate. [SCREEN:demo.mp4]"

Slide 3: Summary
Speaker Notes: "To summarize, we covered three main points. Thank you for watching!"
```

**Generate Video:**
```powershell
python _video_automation/video_creator.py module_02.pptx --voice amit --captions --chapters
```

**📖 Full Documentation:**
See `_video_automation/README_VIDEO.md` for complete guide, examples, and advanced features.

---

## ⚙️ System Requirements

### Required Files Summary:
- ✅ Python 3.12 installed
- ✅ Chatterbox TTS package
- ✅ PyTorch and dependencies
- ✅ Reference audio files

### Check Your Installation:
```powershell
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import chatterbox; print('Chatterbox: OK')"
```

---

## 📊 Performance

| Hardware | Speed | 10-minute audio |
|----------|-------|-----------------|
| CPU only | ~10 sec/sentence | ~20 minutes |
| NVIDIA GPU | ~1-2 sec/sentence | ~2-3 minutes |

Your system: **CPU only** (no GPU detected)

---

## 🎵 Audio Output

- **Format:** WAV (24kHz, 16-bit PCM)
- **Quality:** High-quality speech synthesis
- **Length:** Any length (automatically chunked)

---

## 📝 Common Commands

### Generate from text file:
```powershell
python amit_narrate.py script.txt
```

### Generate with Saanvi's voice:
```powershell
python clone_saanvi_voice.py
```

### Combine multiple audio files:
```powershell
python _scripts/combine_audio_files.py
```

### Check what's generating:
- Look in `Amit_Clone/` or `Saanvi_Clone/` folders
- Newest file = latest generation

---

## 🧹 Cleanup Guide

### Safe to Delete:
- ✅ `_archive/` folder (old test files)
- ✅ Individual `cloned_output_*.wav` files
- ✅ `output.wav`
- ✅ Test scripts in `_archive/`

### Keep These:
- ❌ **DO NOT DELETE** `_reference_audio/` folder
- ❌ **DO NOT DELETE** main script files
- ❌ **DO NOT DELETE** `module_02_video_script.md`

### Output Management:
```powershell
# Delete old outputs (keep only recent)
cd Amit_Clone
del /Q amit_*.wav  # Careful: deletes all Amit outputs

# Or move to backup
mkdir backup
move amit_*.wav backup/
```

---

## 🛠️ Troubleshooting

### Script won't run:
```powershell
# Check Python
python --version

# Check you're in the right folder
cd C:\Work\code\Voice_Clone\Chartterbox
```

### "Cannot find reference audio":
```powershell
# Check if files exist
ls _reference_audio/
```

### Generation is slow:
- Normal for CPU (10 sec/sentence)
- Consider GPU upgrade for 5-10x speed

---

## 📚 Documentation

Detailed guides available in `_docs/` folder:
- **VOICE_CLONES_QUICK_REFERENCE.md** - Quick commands
- **AUDIO_LENGTH_GUIDE.md** - Length limits and optimization
- **VOICE_CLONING_GUIDE.md** - Complete guide

---

## 💡 Tips

1. **For long scripts:** Use `amit_narrate.py` with text file
2. **Test first:** Generate a short test before long scripts
3. **Backup:** Keep copies of your reference audio files
4. **Organize:** Put generated files in dated folders
5. **Clean up:** Regularly delete old test outputs

---

## 🎯 Quick Reference Card

| Task | Command |
|------|---------|
| Generate Amit's voice | `python amit_narrate.py script.txt` |
| Generate Saanvi's voice | `python clone_saanvi_voice.py` |
| Combine audio files | `python _scripts/combine_audio_files.py` |
| Check GPU | `python -c "import torch; print(torch.cuda.is_available())"` |

---

## ✅ Current Status

- ✅ Chatterbox TTS installed
- ✅ 2 voice clones configured (Amit + Saanvi)
- ✅ All dependencies installed
- ✅ System ready to use
- ℹ️ CPU-only mode (slower but works perfectly)

---

## 📞 Need Help?

Check documentation in `_docs/` folder or review:
- Main scripts have comments explaining usage
- Error messages usually indicate missing files
- Make sure you're in the correct directory

---

**Last Updated:** February 11, 2026
**System:** Windows 11, Python 3.12, CPU Mode
