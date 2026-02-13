# Chatterbox Voice Clone & Video Automation

Complete AI-powered voice cloning and video automation system featuring:
- 🎤 **Voice Cloning** with Chatterbox TTS (Amit & Saanvi voices)
- 🎬 **Video Automation** - PowerPoint → Professional Videos
- 🎨 **Snowbrix Slide Design** - Branded presentation system
- 🖼️ **AI Image Generation** - Google Gemini/Imagen integration

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/amitkoti/chatterbox-voice-clone)

---

## 🚀 Quick Start

### Voice Cloning
```powershell
# Generate audio with Amit's voice
python amit_narrate.py your_script.txt

# Generate audio with Saanvi's voice
python clone_saanvi_voice.py
```

### Video Automation
```powershell
# Install dependencies
pip install -r requirements.txt

# Create video from PowerPoint
python _video_automation/video_creator.py your_slides.pptx --voice amit
```

---

## 📁 Project Structure

```
chatterbox-voice-clone/
│
├── requirements.txt              # 📦 All dependencies (consolidated)
├── README.md                     # 📖 This file
│
├── Voice Cloning Scripts:
│   ├── amit_narrate.py           # Generate Amit's voice (from file)
│   ├── clone_amit_voice.py       # Generate Amit's voice (paste script)
│   └── clone_saanvi_voice.py     # Generate Saanvi's voice
│
├── _reference_audio/             # 🎤 Voice samples (REQUIRED)
│   ├── audio_sample.wav          # Amit's voice reference
│   └── Saanvi_Voice_Clone.wav    # Saanvi's voice reference
│
├── _scripts/                     # 🔧 Utility scripts
│   ├── combine_audio_files.py    # Combine multiple audio files
│   └── generate_long_audio.py    # Universal long audio generator
│
├── _video_automation/            # 🎬 Video Creation System
│   ├── Core Modules:
│   │   ├── video_creator.py          # Main video automation CLI
│   │   ├── video_composer.py         # Video assembly engine
│   │   ├── ppt_parser.py             # PowerPoint parser
│   │   ├── slide_redesigner_v2.py    # Slide redesigner (current)
│   │   ├── slide_composer_snowbrix.py # Snowbrix brand composer
│   │   ├── slide_composer.py         # Base slide composer
│   │   ├── snowbrix_layouts_complete.py # Complete layout system
│   │   ├── image_generator.py        # AI image generation
│   │   ├── prompt_generator.py       # AI prompt generation
│   │   ├── api_manager.py            # Multi-account API manager
│   │   ├── config_manager.py         # Configuration management
│   │   └── inventory_manager.py      # Project inventory
│   │
│   ├── Brand System:
│   │   ├── brand_colors_snowbrix.py  # Snowbrix colors (current)
│   │   ├── brand_colors.py           # Base brand colors
│   │   └── Snowbrix_TextOnly_Full_Cream.png # Reference logo
│   │
│   ├── examples/                 # 📚 Examples & Tools
│   │   ├── demos/               # Demo scripts (7 files)
│   │   ├── tests/               # Test scripts (5 files)
│   │   ├── tools/               # Utility tools (4 files)
│   │   ├── sample_config.json   # Example configuration
│   │   ├── sample_presentation.pptx # Sample PowerPoint
│   │   └── README.md            # Examples documentation
│   │
│   ├── docs/                     # 📖 Video automation guides
│   │   ├── README_VIDEO.md          # Main video guide
│   │   ├── QUICK_START.md           # Quick start guide
│   │   ├── WORKFLOW_GUIDE.md        # Workflow documentation
│   │   ├── SETUP_COMPLETE.md        # Setup instructions
│   │   ├── BRAND_STYLES_GUIDE.md    # Brand style guide
│   │   ├── COLOR_PALETTE_GUIDE.md   # Color palette reference
│   │   └── GOOGLE_API_SETUP.md      # Google API setup
│   │
│   └── _projects/                # 🎞️ Generated video projects
│       └── [project_name]/       # Individual project folders
│           ├── images/           # Generated slide backgrounds
│           ├── image_prompts/    # AI prompts used
│           ├── slides_rendered/  # Rendered slide images
│           └── output/           # Final videos & audio
│
├── _docs/                        # 📚 Voice cloning documentation
│   ├── VOICE_CLONING_GUIDE.md    # Complete voice cloning guide
│   ├── VOICE_CLONES_QUICK_REFERENCE.md # Quick reference
│   └── AUDIO_LENGTH_GUIDE.md     # Audio length guidelines
│
├── Output Folders (Generated):
│   ├── Amit_Clone/              # Amit's audio outputs
│   └── Saanvi_Clone/            # Saanvi's audio outputs
│
└── Snowflake_Template_2025.pptx # 📊 Reference template

Note: All generated outputs (images, audio, video) are gitignored
```

---

## ✨ Features

### 🎤 Voice Cloning
- **Multiple Voices:** Amit (professional male) & Saanvi (female)
- **High Quality:** 24kHz, 16-bit PCM WAV output
- **Any Length:** Automatic chunking for long scripts
- **Fast Generation:** ~10 sec/sentence on CPU
- **Custom Voices:** Add your own voice samples

### 🎬 Video Automation
- **PowerPoint Integration:** Convert slides + notes → video
- **AI Narration:** Automatic voice-over from speaker notes
- **Smart Timing:** Per-slide audio synchronization
- **Professional Output:** H.264/AAC, YouTube-ready
- **Batch Processing:** Process multiple presentations

### 🎨 Snowbrix Slide Design
- **Professional Brand:** Cream + green color palette
- **15 Layouts:** Title, content, columns, quotes, sections
- **Consistent Style:** Typography, spacing, alignment
- **Auto-formatting:** Numbered points, bullets, images
- **Template System:** Reusable presentation templates

### 🖼️ AI Image Generation
- **Google Gemini:** Imagen 3.0 integration
- **Brand-Aware:** Auto-generates Snowbrix-styled images
- **Smart Prompts:** Context-aware prompt generation
- **Multi-Account:** Automatic API key rotation
- **16:9 Output:** Perfect for presentation slides

---

## 📦 Installation

### Prerequisites
- Python 3.12+
- Windows 11 (or Windows 10)
- FFmpeg (for video processing)

### Step 1: Install FFmpeg
```powershell
# Using winget (recommended)
winget install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

### Step 2: Install Python Dependencies
```powershell
# Install all dependencies
pip install -r requirements.txt
```

### Step 3: Set Up Chatterbox TTS
Follow instructions in `_docs/VOICE_CLONING_GUIDE.md`

### Step 4: Configure Google API (Optional)
For AI image generation:
```powershell
python _video_automation/examples/tools/setup_google_api.py
```

---

## 🎯 Usage Examples

### 1. Voice Cloning - Simple

**Generate audio from text file:**
```powershell
# Create your script
notepad my_script.txt

# Generate audio
python amit_narrate.py my_script.txt

# Output: Amit_Clone/amit_TIMESTAMP.wav
```

### 2. Voice Cloning - Long Form

**Generate long-form content:**
```python
# Use the utility script
from _scripts.generate_long_audio import generate_long_audio

text = """
Your long script here...
Multiple paragraphs...
"""

generate_long_audio(
    text=text,
    reference_audio="_reference_audio/audio_sample.wav",
    output_path="output.wav",
    progress_callback=lambda x: print(f"Progress: {x}%")
)
```

### 3. Video Automation - Basic

**Create video from PowerPoint:**
```powershell
python _video_automation/video_creator.py presentation.pptx \
    --voice amit \
    --output my_video.mp4
```

### 4. Video Automation - Advanced

**With all options:**
```powershell
python _video_automation/video_creator.py module_02.pptx \
    --voice amit \
    --pause 1.5 \
    --resolution 1920x1080 \
    --fps 30 \
    --output output/module_02_final.mp4
```

### 5. Slide Redesign

**Redesign PowerPoint with Snowbrix brand:**
```powershell
python _video_automation/slide_redesigner_v2.py old_slides.pptx \
    --brand snowbrix \
    --generate-images \
    --output new_slides.pptx
```

---

## 🔧 Configuration

### Voice Clone Configuration

Edit scripts to customize:
- Voice selection (Amit/Saanvi)
- Output directory
- Audio format settings

### Video Automation Configuration

Create `api_keys.json` in `_video_automation/`:
```json
{
  "google_api_keys": [
    "YOUR_GOOGLE_API_KEY_1",
    "YOUR_GOOGLE_API_KEY_2"
  ]
}
```

See `_video_automation/api_keys.example.json` for template.

---

## 📊 System Requirements

### Minimum Requirements
- **OS:** Windows 10/11
- **CPU:** Intel i5 or equivalent
- **RAM:** 8GB
- **Storage:** 5GB free space
- **Python:** 3.12+

### Recommended Requirements
- **CPU:** Intel i7 or AMD Ryzen 7
- **RAM:** 16GB
- **GPU:** NVIDIA GPU with CUDA (10x faster voice cloning)
- **Storage:** 20GB free space

### Performance Benchmarks

| Task | CPU (i5) | CPU (i7) | GPU (NVIDIA) |
|------|----------|----------|--------------|
| Voice cloning (10 min) | ~20 min | ~15 min | ~2-3 min |
| Video rendering (5 min) | ~3 min | ~2 min | ~1 min |
| Image generation (1 image) | N/A | N/A | ~10 sec |

---

## 📚 Documentation

### Voice Cloning Guides
- [`_docs/VOICE_CLONING_GUIDE.md`](_docs/VOICE_CLONING_GUIDE.md) - Complete guide
- [`_docs/VOICE_CLONES_QUICK_REFERENCE.md`](_docs/VOICE_CLONES_QUICK_REFERENCE.md) - Quick commands
- [`_docs/AUDIO_LENGTH_GUIDE.md`](_docs/AUDIO_LENGTH_GUIDE.md) - Length optimization

### Video Automation Guides
- [`_video_automation/README_VIDEO.md`](_video_automation/README_VIDEO.md) - Main video guide
- [`_video_automation/QUICK_START.md`](_video_automation/QUICK_START.md) - Quick start
- [`_video_automation/WORKFLOW_GUIDE.md`](_video_automation/WORKFLOW_GUIDE.md) - Workflow
- [`_video_automation/BRAND_STYLES_GUIDE.md`](_video_automation/BRAND_STYLES_GUIDE.md) - Brand guide

### Examples
- [`_video_automation/examples/README.md`](_video_automation/examples/README.md) - Examples overview

---

## 🛠️ Troubleshooting

### Voice Cloning Issues

**"Cannot find reference audio"**
```powershell
# Verify files exist
ls _reference_audio/
```

**Slow generation**
- Normal for CPU: ~10 sec/sentence
- Consider GPU for 10x speedup
- Use progress callbacks to monitor

### Video Automation Issues

**"FFmpeg not found"**
```powershell
# Install FFmpeg
winget install ffmpeg

# Verify installation
ffmpeg -version
```

**"Google API quota exceeded"**
- Add more API keys to `api_keys.json`
- System automatically rotates between keys

**Video/audio sync issues**
- Ensure per-slide audio files are generated
- Check `_calculate_timings()` in video_composer.py

---

## 🧹 Maintenance

### Clean Generated Files
```powershell
# Clean old audio outputs
del Amit_Clone\*.wav
del Saanvi_Clone\*.wav

# Clean video project outputs (keeps source code)
# _projects/*/output/ and _projects/*/images/ are gitignored
```

### Update Dependencies
```powershell
pip install -r requirements.txt --upgrade
```

---

## 🤝 Contributing

This is a personal project, but suggestions are welcome! See the GitHub repository for issues and discussions.

---

## 📝 License

This project uses:
- **Chatterbox TTS** - Check Chatterbox license
- **Google Gemini API** - Google Cloud terms apply
- **MoviePy** - MIT License
- **python-pptx** - MIT License

---

## 🎯 Roadmap

- [ ] Add more voice clones
- [ ] Support for other TTS engines (ElevenLabs, Azure)
- [ ] Video templates library
- [ ] Automated chapter markers
- [ ] Subtitle generation
- [ ] Multi-language support
- [ ] Web interface

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub](https://github.com/amitkoti/chatterbox-voice-clone)
- Check the documentation in `_docs/` and `_video_automation/docs/`

---

## ✅ Current Status

- ✅ Voice cloning fully operational (Amit + Saanvi)
- ✅ Video automation system complete
- ✅ Snowbrix brand design system implemented
- ✅ Google Gemini image generation integrated
- ✅ Repository organized and cleaned
- ✅ All dependencies consolidated
- ✅ Production-ready

---

**Last Updated:** February 13, 2026
**Version:** 2.0
**System:** Windows 11, Python 3.12, CPU Mode
**Repository:** https://github.com/amitkoti/chatterbox-voice-clone
