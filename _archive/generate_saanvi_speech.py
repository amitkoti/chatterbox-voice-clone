"""
Quick Speech Generator for Saanvi's Voice
Use this script to quickly generate any text with Saanvi's cloned voice
"""

import perth
if perth.PerthImplicitWatermarker is None:
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import os
import sys

def save_audio(audio, filename):
    """Helper function to save audio"""
    if hasattr(audio, 'cpu'):
        audio = audio.cpu().numpy()
    audio = audio.squeeze()
    sf.write(filename, audio, 24000, subtype='PCM_16')
    return filename

# ============================================
# CUSTOMIZE YOUR TEXT HERE
# ============================================
CUSTOM_TEXT = "Hello! This is Saanvi speaking."
# ============================================

# Reference audio for Saanvi's voice
REFERENCE_AUDIO = "Saanvi_Voice_Clone.wav"
OUTPUT_DIR = "Saanvi_Clone"

# Check if reference audio exists
if not os.path.exists(REFERENCE_AUDIO):
    print(f"ERROR: Cannot find '{REFERENCE_AUDIO}'")
    print("Please record Saanvi's voice first and save it as 'saanvi_sample.wav'")
    exit(1)

# Create output directory if needed
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("="*60)
print("GENERATING SPEECH WITH SAANVI'S VOICE")
print("="*60)

# Load model (this takes a moment)
print("\nLoading model...")
tts = ChatterboxTTS.from_pretrained(device="cpu")

# Generate speech
print(f"\nGenerating: \"{CUSTOM_TEXT}\"")
audio = tts.generate(CUSTOM_TEXT, audio_prompt_path=REFERENCE_AUDIO)

# Save output
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(OUTPUT_DIR, f"saanvi_speech_{timestamp}.wav")
save_audio(audio, output_file)

print(f"\nSUCCESS! Saved to: {output_file}")
print("\n" + "="*60)

# Usage instructions
print("\nTo generate different text:")
print("1. Edit this script")
print("2. Change the CUSTOM_TEXT variable at the top")
print("3. Run the script again")
print("\nOr use command line:")
print('  python generate_saanvi_speech.py "Your text here"')
