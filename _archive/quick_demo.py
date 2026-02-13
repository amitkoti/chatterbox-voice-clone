"""
Quick Voice Cloning Demo
This script demonstrates voice cloning with Chatterbox.
"""

import perth
if perth.PerthImplicitWatermarker is None:
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import os

def save_audio(audio, filename):
    """Helper function to save audio"""
    if hasattr(audio, 'cpu'):
        audio = audio.cpu().numpy()
    audio = audio.squeeze()
    sf.write(filename, audio, 24000, subtype='PCM_16')
    print(f"  Saved: {filename}")

# Load model
print("="*60)
print("CHATTERBOX VOICE CLONING DEMO")
print("="*60)
print("\nLoading model (this may take a minute)...")
tts = ChatterboxTTS.from_pretrained(device="cpu")
print("Model loaded successfully!\n")

# Demo text
demo_text = "Welcome to Chatterbox! This is an example of voice cloning technology."

# Generate with default voice first
print("Step 1: Generating with default voice...")
audio_default = tts.generate(demo_text)
save_audio(audio_default, "demo_default_voice.wav")

print("\n" + "="*60)
print("VOICE CLONING INSTRUCTIONS")
print("="*60)
print("""
To clone a specific voice:

1. Prepare your reference audio:
   - Record 10-30 seconds of clean speech
   - Save as WAV, MP3, or other common format
   - Place it in this directory

2. Update this script:
   - Find the line: REFERENCE_AUDIO = "your_audio.wav"
   - Replace with your audio filename

3. Run this script again

Example code for voice cloning:
""")

print('''
# Load reference audio
conditionals = tts.prepare_conditionals("reference_audio.wav")

# Generate with cloned voice
audio = tts.generate("Your text here", conditionals=conditionals)

# Save output
audio = audio.cpu().numpy().squeeze()
sf.write("cloned_output.wav", audio, 24000)
''')

# Check if user has provided reference audio
REFERENCE_AUDIO = "reference_audio.wav"  # Change this to your audio file

if os.path.exists(REFERENCE_AUDIO):
    print(f"\nFound reference audio: {REFERENCE_AUDIO}")
    print("Step 2: Cloning voice from reference audio...")

    conditionals = tts.prepare_conditionals(REFERENCE_AUDIO)
    audio_cloned = tts.generate(demo_text, conditionals=conditionals)
    save_audio(audio_cloned, "demo_cloned_voice.wav")

    print("\nSUCCESS! Compare the two files:")
    print("  - demo_default_voice.wav (built-in voice)")
    print("  - demo_cloned_voice.wav (cloned voice)")
else:
    print(f"\nNo reference audio found at: {REFERENCE_AUDIO}")
    print("For now, you have the default voice demo.")

print("\n" + "="*60)
print("Demo complete!")
print("="*60)
