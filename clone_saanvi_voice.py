"""
Saanvi's Voice Cloning Script
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

# Reference audio file for Saanvi's voice
reference_audio = "_reference_audio/Saanvi_Voice_Clone.wav"

# Check if reference audio exists
if not os.path.exists(reference_audio):
    print("="*60)
    print("SAANVI'S VOICE CLONING - SETUP REQUIRED")
    print("="*60)
    print(f"\nPlease record Saanvi's voice and save it as: {reference_audio}")
    print("\nRecording Tips:")
    print("  - 10-30 seconds of clear speech")
    print("  - Quiet environment, no background noise")
    print("  - Natural speaking voice")
    print("  - Multiple sentences work best")
    print("\nOnce you have the recording, run this script again!")
    exit(0)

print("="*60)
print("CLONING SAANVI'S VOICE")
print("="*60)

# Load model
print("\nStep 1: Loading Chatterbox model...")
tts = ChatterboxTTS.from_pretrained(device="cpu")
print("  Model loaded successfully!")

# Test sentences for Saanvi's cloned voice
# You can customize these sentences!
test_sentences = [
    "Hello, my name is Saanvi!",
    "How are you doing today?",
    "I love learning new things every day.",
    "This voice cloning technology is so cool!",
    "Let's go play outside in the sunshine."
]

print(f"\nStep 2: Using '{reference_audio}' as voice reference...")
print("Step 3: Generating speech with Saanvi's cloned voice...")
print("-" * 60)

# Create output directory for Saanvi's cloned voice files
output_dir = "Saanvi_Clone"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}/")

for i, text in enumerate(test_sentences, 1):
    print(f"\n[{i}/{len(test_sentences)}] Generating: \"{text}\"")

    # Generate audio with Saanvi's cloned voice
    audio = tts.generate(text, audio_prompt_path=reference_audio)

    # Save to Saanvi_Clone directory
    filename = os.path.join(output_dir, f"saanvi_clone_{i}.wav")
    save_audio(audio, filename)

print("\n" + "="*60)
print("SUCCESS! Saanvi's voice cloning complete!")
print("="*60)
print(f"\nAll files saved in: {output_dir}/")
print("\nGenerated files:")
for i in range(1, len(test_sentences) + 1):
    print(f"  - {output_dir}/saanvi_clone_{i}.wav")

print("\n" + "="*60)
print("TIPS:")
print("="*60)
print("- Play the files to hear Saanvi's cloned voice")
print("- Edit 'test_sentences' in this script for custom text")
print("- Use longer reference audio for better voice quality")
print("\nTo generate more audio with Saanvi's voice,")
print("just edit the test_sentences list and run this script again!")
