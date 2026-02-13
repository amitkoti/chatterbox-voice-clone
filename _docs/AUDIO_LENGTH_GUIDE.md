# Audio Length Limitations and Best Practices

## Quick Answer

**Short Answer:** You can generate audio of virtually any length, but it's best done in smaller chunks.

**Recommended Approach:**
- **Single generation:** 1-3 sentences (15-30 seconds)
- **Long content:** Split into chunks and combine

## Technical Limitations

### 1. **Per-Generation Limits**
- **Model limit:** ~50-100 words per generation (recommended)
- **Maximum:** Technically can go longer, but quality degrades
- **Memory:** Longer texts use more RAM/VRAM

### 2. **Practical Constraints**
- **Processing time:** ~10-15 seconds per sentence on CPU
- **Quality:** Shorter generations typically have better quality
- **Coherence:** Very long single generations may lose consistency

### 3. **No Hard Limits On:**
- Total project length (combine multiple generations)
- Number of generations you can make
- Final audio file length after combining

## Best Practices for Different Lengths

### Short Audio (< 30 seconds)
✅ **Use single generation**

```python
text = "Your short text here, one to three sentences."
audio = tts.generate(text, audio_prompt_path="reference.wav")
```

### Medium Audio (30 seconds - 2 minutes)
✅ **Split into multiple sentences**

```python
sentences = [
    "First sentence here.",
    "Second sentence here.",
    "Third sentence here."
]

outputs = []
for sentence in sentences:
    audio = tts.generate(sentence, audio_prompt_path="reference.wav")
    outputs.append(audio.cpu().numpy().squeeze())

# Combine
import numpy as np
combined = np.concatenate(outputs)
sf.write("output.wav", combined, 24000)
```

### Long Audio (> 2 minutes)
✅ **Generate in chunks and combine**

```python
# Split long text into paragraphs or logical chunks
chunks = [
    "First paragraph of your long text...",
    "Second paragraph of your long text...",
    "Third paragraph of your long text..."
]

for i, chunk in enumerate(chunks):
    audio = tts.generate(chunk, audio_prompt_path="reference.wav")
    sf.write(f"part_{i}.wav", audio.cpu().numpy().squeeze(), 24000)

# Then use audio editing software to combine, or use Python
```

## Example: Generate Long Content

### Audiobook/Story Script

```python
import perth
if perth.PerthImplicitWatermarker is None:
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import numpy as np

# Load model once
tts = ChatterboxTTS.from_pretrained(device="cpu")

# Your long story split into sentences
story = """
Once upon a time, there was a little girl named Saanvi.
She loved to explore the world around her.
Every day was a new adventure.
One sunny morning, she found a magical garden.
The flowers sparkled with rainbow colors.
"""

# Split into sentences
import re
sentences = [s.strip() for s in re.split(r'[.!?]+', story) if s.strip()]

print(f"Generating {len(sentences)} sentences...")

audio_chunks = []
for i, sentence in enumerate(sentences, 1):
    print(f"[{i}/{len(sentences)}] {sentence}")
    audio = tts.generate(sentence, audio_prompt_path="Saanvi_Voice_Clone.wav")
    audio_chunks.append(audio.cpu().numpy().squeeze())

    # Optional: Save individual chunks
    sf.write(f"story_part_{i}.wav", audio_chunks[-1], 24000)

# Combine all chunks
combined_audio = np.concatenate(audio_chunks)
sf.write("full_story.wav", combined_audio, 24000)

print(f"Complete! Generated {len(combined_audio)/24000:.1f} seconds of audio")
```

## Combining Audio Files

### Method 1: Using Python (numpy)
```python
import soundfile as sf
import numpy as np

# Read all parts
parts = []
for i in range(1, 11):  # 10 parts
    audio, sr = sf.read(f"part_{i}.wav")
    parts.append(audio)

# Combine
combined = np.concatenate(parts)
sf.write("complete_audio.wav", combined, 24000)
```

### Method 2: Using pydub (with silence between)
```python
from pydub import AudioSegment

# Load parts
audio = AudioSegment.from_wav("part_1.wav")
for i in range(2, 11):
    # Add 500ms silence between parts
    audio += AudioSegment.silent(duration=500)
    audio += AudioSegment.from_wav(f"part_{i}.wav")

audio.export("complete_audio.wav", format="wav")
```

## Performance Tips

### For Long Audio Generation:

1. **Use batching:**
   - Generate 10-20 sentences at a time
   - Save intermediate results
   - Prevents memory issues

2. **Processing time estimates:**
   - CPU: ~10-15 seconds per sentence
   - GPU (CUDA): ~1-2 seconds per sentence
   - 10-minute audiobook: ~1-2 hours on CPU

3. **Memory management:**
   ```python
   import gc
   import torch

   # After every 10 generations
   gc.collect()
   if torch.cuda.is_available():
       torch.cuda.empty_cache()
   ```

## Recommended Workflow for Very Long Content

### For Audiobooks, Long Stories, etc.:

1. **Prepare text:**
   - Split into chapters/sections
   - Break into sentences
   - Remove special characters

2. **Generate in sessions:**
   ```python
   # Generate Chapter 1 (30 minutes)
   # Save and combine

   # Generate Chapter 2 (30 minutes)
   # Save and combine

   # etc.
   ```

3. **Combine final chapters:**
   - Use audio editing software (Audacity, Adobe Audition)
   - Or use Python pydub/numpy

## Example: Complete Long Audio Generator

I'll create a script for you that handles any length automatically!

```python
# See: generate_long_audio.py (created next)
```

## Real-World Examples

### What You Can Create:

| Content Type | Length | Chunks Needed | Time (CPU) |
|--------------|--------|---------------|------------|
| Short message | 10 sec | 1 | 10 sec |
| Poem | 1 min | 3-5 | 1 min |
| Short story | 5 min | 15-20 | 5 min |
| Article | 10 min | 40-50 | 10 min |
| Chapter | 30 min | 120-150 | 30 min |
| Audiobook | 5 hours | 2000+ | 8-10 hours |

## Summary

✅ **No hard limit** on total audio length
✅ **Best practice:** Generate 1-3 sentences at a time
✅ **For long content:** Split, generate, combine
✅ **Quality:** Shorter chunks = better consistency
✅ **Speed:** Use GPU for faster generation

**Bottom line:** You can create audio of any length - just break it into manageable chunks!
