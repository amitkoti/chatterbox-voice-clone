# Workaround for missing PerthImplicitWatermarker
import perth
if perth.PerthImplicitWatermarker is None:
    print("Note: Using DummyWatermarker (Perth watermarker not available)")
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS

print("Loading Chatterbox model...")
tts_model = ChatterboxTTS.from_pretrained(device="cpu")
print("Generating audio for 'Hello world'...")
audio = tts_model.generate("Hello world")

print(f"Audio type: {type(audio)}, shape: {audio.shape if hasattr(audio, 'shape') else 'N/A'}")

import soundfile as sf
import numpy as np

# Convert to numpy array if it's a tensor
if hasattr(audio, 'cpu'):
    audio = audio.cpu().numpy()

# Ensure it's the right shape for soundfile (samples,) or (samples, channels)
if len(audio.shape) > 1:
    audio = audio.squeeze()

sf.write("output.wav", audio, 24000, subtype='PCM_16')  # Chatterbox uses 24kHz sample rate

print("SUCCESS: Audio generated successfully! Check 'output.wav' in the current directory.")
