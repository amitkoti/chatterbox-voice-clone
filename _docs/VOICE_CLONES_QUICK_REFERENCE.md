# Voice Clones - Quick Reference Guide

## 🎤 Your Voice Clones

You have **3 voice clones** set up:

### 1. **Amit's Voice** (Your Voice)
- **Reference Audio:** `audio_sample.wav`
- **Output Folder:** `Amit_Clone/`

### 2. **Saanvi's Voice** (Daughter's Voice)
- **Reference Audio:** `Saanvi_Voice_Clone.wav`
- **Output Folder:** `Saanvi_Clone/`

### 3. **Original Test Voice**
- **Reference Audio:** `audio_sample.wav`
- **Output Files:** `cloned_output_*.wav`

---

## 🚀 How to Generate Audio

### Option 1: Amit's Voice (Recommended for Long Scripts)

#### Method A: Edit script in file
```bash
# 1. Open clone_amit_voice.py
# 2. Find YOUR_SCRIPT = """..."""
# 3. Paste your script between the quotes
# 4. Run:
python clone_amit_voice.py
```

#### Method B: From text file
```bash
# 1. Create a file called amit_script.txt
# 2. Paste your script in it
# 3. Run:
python amit_narrate.py amit_script.txt
```

### Option 2: Saanvi's Voice

#### Method A: Edit script in file
```bash
# 1. Open clone_saanvi_voice.py
# 2. Edit test_sentences = [...]
# 3. Run:
python clone_saanvi_voice.py
```

#### Method B: Quick generator
```bash
# 1. Open generate_saanvi_speech.py
# 2. Change CUSTOM_TEXT = "..."
# 3. Run:
python generate_saanvi_speech.py
```

---

## 📂 File Structure

```
C:\Work\code\Voice_Clone\Chartterbox\
│
├── Reference Audio Files:
│   ├── audio_sample.wav            # Amit's voice
│   └── Saanvi_Voice_Clone.wav      # Saanvi's voice
│
├── Amit's Voice Tools:
│   ├── clone_amit_voice.py         # Main script (paste text inside)
│   └── amit_narrate.py             # From text file
│
├── Saanvi's Voice Tools:
│   ├── clone_saanvi_voice.py       # Main script
│   └── generate_saanvi_speech.py   # Quick generator
│
├── Universal Tools:
│   ├── generate_long_audio.py      # Any voice, long content
│   └── combine_audio_files.py      # Combine multiple files
│
└── Output Folders:
    ├── Amit_Clone/                 # Amit's audio
    └── Saanvi_Clone/               # Saanvi's audio
```

---

## 📝 Quick Examples

### Generate Short Audio (Amit)
```python
# Open clone_amit_voice.py

YOUR_SCRIPT = """
Hello everyone. This is Amit speaking.
Welcome to this presentation.
"""

# Then run: python clone_amit_voice.py
```

### Generate Long Story (Amit)
1. Create `amit_script.txt`:
```
Once upon a time, in a land far away...
[Your full story here - any length!]
The end.
```

2. Run:
```bash
python amit_narrate.py amit_script.txt
```

### Generate with Saanvi's Voice
```python
# Open generate_saanvi_speech.py

CUSTOM_TEXT = "Hello daddy! I love you so much!"

# Then run: python generate_saanvi_speech.py
```

---

## ⚡ Quick Commands Cheat Sheet

### Amit (Your Voice)
```bash
# From script in file
python clone_amit_voice.py

# From text file
python amit_narrate.py your_script.txt
```

### Saanvi (Daughter's Voice)
```bash
# Main script
python clone_saanvi_voice.py

# Quick generator
python generate_saanvi_speech.py
```

### Long Audio (Any Voice)
```bash
# Edit generate_long_audio.py and set:
# VOICE_REFERENCE = "audio_sample.wav"  # for Amit
# or
# VOICE_REFERENCE = "Saanvi_Voice_Clone.wav"  # for Saanvi

python generate_long_audio.py
```

### Combine Multiple Files
```bash
python combine_audio_files.py
```

---

## 💡 Tips

### For Best Quality:
1. **Reference audio:** 10-30 seconds of clear speech
2. **Text:** Split into sentences (automatic)
3. **Length:** Any length works - it's automatically chunked

### Processing Time:
- **Short (30 sec):** ~30 seconds
- **Medium (5 min):** ~5 minutes
- **Long (30 min):** ~30 minutes

### Faster Generation:
If you have an NVIDIA GPU, change:
```python
device="cpu"  →  device="cuda"
```
This will be 5-10x faster!

---

## 🎯 Common Tasks

### Task: Narrate a Story with Amit's Voice
```bash
1. Save story as amit_story.txt
2. python amit_narrate.py amit_story.txt
3. Find output in Amit_Clone/
```

### Task: Create Personalized Message with Saanvi's Voice
```bash
1. Open generate_saanvi_speech.py
2. Change CUSTOM_TEXT = "Your message here"
3. python generate_saanvi_speech.py
```

### Task: Generate Audiobook Chapter (Either Voice)
```bash
1. Create chapter1.txt with chapter content
2. python amit_narrate.py chapter1.txt
   # Output: Amit_Clone/amit_TIMESTAMP.wav
```

### Task: Combine Multiple Audio Files
```bash
python combine_audio_files.py
# Follow the interactive prompts
```

---

## 🆘 Troubleshooting

### Error: "Cannot find reference audio"
- Make sure you're in the correct directory
- Check that audio_sample.wav exists for Amit
- Check that Saanvi_Voice_Clone.wav exists for Saanvi

### Output Quality Issues
- Use longer reference audio (20-30 seconds)
- Ensure reference audio is clear (no background noise)
- Try recording new reference audio

### Slow Generation
- Normal on CPU: ~10 seconds per sentence
- For faster: Use GPU (device="cuda")
- Or generate overnight for very long content

---

## 📞 Quick Start Right Now

Want to test Amit's voice right now?

1. **Create a file:** `test_script.txt`
2. **Add text:**
   ```
   Hello, this is Amit. This is a test of my cloned voice.
   I can narrate any script you provide.
   ```
3. **Run:**
   ```bash
   python amit_narrate.py test_script.txt
   ```

4. **Listen:** Check `Amit_Clone/` folder!

---

## Summary

✅ **Amit's Voice:** Use `clone_amit_voice.py` or `amit_narrate.py`
✅ **Saanvi's Voice:** Use `clone_saanvi_voice.py` or `generate_saanvi_speech.py`
✅ **Any Length:** All scripts handle long content automatically
✅ **Easy to Use:** Just paste text and run!

**Ready to generate your script!** 🎤
