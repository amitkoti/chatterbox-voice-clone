# Voice Cloning Guide for Chatterbox

## Quick Start

### Step 1: Prepare Your Reference Audio

**Requirements:**
- **Duration:** 10-30 seconds (longer is better, up to 1-2 minutes)
- **Quality:** Clear audio, minimal background noise
- **Format:** WAV, MP3, FLAC, or any common audio format
- **Content:** The person speaking naturally (any content is fine)

**Tips for Best Results:**
- Use high-quality recordings
- Avoid music or sound effects in the background
- Multiple sentences with varied intonation work best
- Studio or quiet room recordings are ideal

### Step 2: Run the Voice Cloning Script

```python
from chatterbox import ChatterboxTTS

# Load model
tts = ChatterboxTTS.from_pretrained(device="cpu")

# Prepare voice from reference audio
conditionals = tts.prepare_conditionals("path/to/reference_audio.wav")

# Generate speech with cloned voice
audio = tts.generate("Your text here", conditionals=conditionals)
```

### Step 3: Save the Output

```python
import soundfile as sf
import numpy as np

# Convert to numpy if needed
if hasattr(audio, 'cpu'):
    audio = audio.cpu().numpy()
audio = audio.squeeze()

# Save as WAV file
sf.write("output.wav", audio, 24000)
```

## Complete Example

```python
# voice_clone.py
import perth
if perth.PerthImplicitWatermarker is None:
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf

# Load model
print("Loading model...")
tts = ChatterboxTTS.from_pretrained(device="cpu")

# Clone voice
print("Cloning voice...")
conditionals = tts.prepare_conditionals("my_voice_sample.wav")

# Generate speech
print("Generating speech...")
audio = tts.generate("Hello world, this is my cloned voice!", conditionals=conditionals)

# Save
audio = audio.cpu().numpy().squeeze()
sf.write("cloned_output.wav", audio, 24000)
print("Done!")
```

## Advanced Usage

### Multiple Sentences
```python
texts = [
    "This is the first sentence.",
    "Here's another one with my cloned voice.",
    "And a third for good measure."
]

for i, text in enumerate(texts):
    audio = tts.generate(text, conditionals=conditionals)
    audio = audio.cpu().numpy().squeeze()
    sf.write(f"output_{i}.wav", audio, 24000)
```

### Batch Processing
```python
# Clone multiple voices
voices = {
    "person1": "audio/person1_sample.wav",
    "person2": "audio/person2_sample.wav"
}

for name, audio_path in voices.items():
    conds = tts.prepare_conditionals(audio_path)
    audio = tts.generate(f"Hello, I am {name}", conditionals=conds)
    audio = audio.cpu().numpy().squeeze()
    sf.write(f"{name}_output.wav", audio, 24000)
```

## Common Issues & Solutions

### Issue: Poor Voice Quality
**Solution:** Use longer, clearer reference audio (20-30 seconds minimum)

### Issue: Voice doesn't sound like the reference
**Solution:**
- Ensure reference audio is clean (no background noise)
- Try a longer sample
- Use audio with natural speech patterns

### Issue: Out of Memory
**Solution:** Use device="cpu" instead of "cuda" for lower memory usage

### Issue: Slow Generation
**Solution:**
- Use GPU if available: `device="cuda"`
- Generate shorter texts
- Consider using a more powerful machine

## Recording Tips for Reference Audio

1. **Use a good microphone** - Built-in laptop mics work, but external USB mics are better
2. **Record in a quiet room** - Close windows, turn off fans/AC
3. **Speak naturally** - Don't try to sound different
4. **Include variety** - Different emotions, questions, statements
5. **Check levels** - Not too quiet, not clipping/distorting

## Supported Audio Formats

Chatterbox can read:
- WAV (recommended)
- MP3
- FLAC
- OGG
- M4A
- And most other common audio formats

## Performance Notes

- **CPU Mode:** 3-5 seconds per sentence
- **GPU Mode:** 0.5-1 second per sentence (requires CUDA GPU)
- **Memory:** ~2-4GB RAM required

## Legal & Ethical Considerations

⚠️ **Important:**
- Only clone voices with explicit permission
- Don't use for impersonation or fraud
- Respect copyright and privacy laws
- Consider disclosure when using cloned voices publicly

## Next Steps

1. Record or obtain a reference audio sample
2. Run `voice_clone_example.py`
3. Experiment with different texts
4. Fine-tune by adjusting reference audio length

For more information, visit:
- GitHub: https://github.com/resemble-ai/chatterbox
- Tutorials: https://medium.com/aimonks/clone-any-voice-using-resemble-ais-chatterbox-a-hands-on-tutorial-9f4ec2f032f8
