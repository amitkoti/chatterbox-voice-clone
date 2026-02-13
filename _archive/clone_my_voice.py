"""
Voice Cloning Script - Using audio_sample.wav
"""

import perth
if perth.PerthImplicitWatermarker is None:
    print("Note: Using DummyWatermarker")
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
    return filename

# Check if reference audio exists
reference_audio = "audio_sample.wav"
if not os.path.exists(reference_audio):
    print(f"ERROR: Could not find '{reference_audio}'")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    exit(1)

print("="*60)
print("VOICE CLONING WITH YOUR AUDIO SAMPLE")
print("="*60)

# Load model
print("\nStep 1: Loading Chatterbox model...")
tts = ChatterboxTTS.from_pretrained(device="cpu")
print("  Model loaded successfully!")

# Test sentences to generate with your cloned voice
test_sentences = [
    "Hello, this is a test of my cloned voice.",
    "The quick brown fox jumps over the lazy dog.",
    "Voice cloning technology is truly amazing!",
    "I can now make my voice say anything I want."
]

print(f"\nStep 2: Using '{reference_audio}' as voice reference...")
print("Step 3: Generating speech with your cloned voice...")
print("-" * 60)

for i, text in enumerate(test_sentences, 1):
    print(f"\n[{i}/{len(test_sentences)}] Generating: \"{text}\"")

    # Generate audio with cloned voice (pass audio_prompt_path parameter)
    audio = tts.generate(text, audio_prompt_path=reference_audio)

    # Save the output
    filename = f"cloned_output_{i}.wav"
    save_audio(audio, filename)

print("\n" + "="*60)
print("SUCCESS! Voice cloning complete!")
print("="*60)
print("\nGenerated files:")
for i in range(1, len(test_sentences) + 1):
    print(f"  - cloned_output_{i}.wav")

print("\nPlay these files to hear your cloned voice!")
print("\nTo generate custom text, edit the 'test_sentences' list in this script.")
