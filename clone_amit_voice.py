"""
Amit's Voice Cloning Script
Generates long audio from your provided script
"""

import perth
if perth.PerthImplicitWatermarker is None:
    print("Note: Using DummyWatermarker")
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import numpy as np
import re
import os
from datetime import datetime

def split_into_sentences(text):
    """Split text into sentences for better quality"""
    # Split on sentence endings
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Clean up empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def save_audio(audio, filename):
    """Helper function to save audio"""
    if hasattr(audio, 'cpu'):
        audio = audio.cpu().numpy()
    audio = audio.squeeze()
    sf.write(filename, audio, 24000, subtype='PCM_16')
    return filename

# ============================================
# CONFIGURATION
# ============================================

# Amit's voice reference
REFERENCE_AUDIO = "_reference_audio/audio_sample.wav"

# OUTPUT DIRECTORY
OUTPUT_DIR = "Amit_Clone"

# ============================================
# YOUR SCRIPT HERE
# ============================================
# Paste your long script/text below between the triple quotes

YOUR_SCRIPT = """
Hello, my name is Amit.

This is a demonstration of voice cloning technology.

I can narrate any script or story you provide.

The system will automatically split this into sentences.
And generate natural-sounding speech for each one.

You can use this for audiobooks, narrations, presentations,
or any other content you need to vocalize.

Simply paste your script above and run this program.
"""

# ============================================
# GENERATE AUDIO
# ============================================

if __name__ == "__main__":
    # Check if reference audio exists
    if not os.path.exists(REFERENCE_AUDIO):
        print("="*60)
        print("ERROR: Reference audio not found!")
        print("="*60)
        print(f"\nCannot find: {REFERENCE_AUDIO}")
        print("\nPlease ensure your voice sample is saved as 'audio_sample.wav'")
        exit(1)

    print("="*60)
    print("AMIT'S VOICE CLONING - LONG AUDIO GENERATOR")
    print("="*60)

    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}/")

    # Split script into sentences
    sentences = split_into_sentences(YOUR_SCRIPT)
    total_sentences = len(sentences)

    if total_sentences == 0:
        print("\nERROR: No text found in YOUR_SCRIPT!")
        print("Please paste your script in the YOUR_SCRIPT variable above.")
        exit(1)

    # Show info
    print(f"\nReference voice: {REFERENCE_AUDIO}")
    print(f"Total sentences: {total_sentences}")
    print(f"Estimated time: ~{total_sentences * 10} seconds on CPU")
    print(f"Output directory: {OUTPUT_DIR}/")

    # Load model
    print("\nStep 1: Loading Chatterbox model...")
    tts = ChatterboxTTS.from_pretrained(device="cpu")
    print("  Model loaded successfully!")

    # Generate timestamp for this session
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(OUTPUT_DIR, f"session_{timestamp}")
    os.makedirs(session_dir, exist_ok=True)

    print(f"\nStep 2: Generating audio with Amit's cloned voice...")
    print("-" * 60)

    audio_chunks = []
    start_time = datetime.now()

    for i, sentence in enumerate(sentences, 1):
        # Show progress
        preview = sentence[:60] + "..." if len(sentence) > 60 else sentence
        print(f"[{i}/{total_sentences}] {preview}")

        # Generate audio
        audio = tts.generate(sentence, audio_prompt_path=REFERENCE_AUDIO)

        # Convert and store
        audio_np = audio.cpu().numpy().squeeze()
        audio_chunks.append(audio_np)

        # Save individual part
        part_file = os.path.join(session_dir, f"part_{i:04d}.wav")
        sf.write(part_file, audio_np, 24000, subtype='PCM_16')

    # Calculate time taken
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("\n" + "-" * 60)
    print("Step 3: Combining all audio chunks...")

    # Combine all chunks
    combined_audio = np.concatenate(audio_chunks)

    # Save combined audio
    combined_file = os.path.join(OUTPUT_DIR, f"amit_complete_{timestamp}.wav")
    sf.write(combined_file, combined_audio, 24000, subtype='PCM_16')

    # Calculate audio length
    audio_length = len(combined_audio) / 24000  # seconds

    print("\n" + "="*60)
    print("SUCCESS! Audio generation complete!")
    print("="*60)
    print(f"\nComplete audio: {combined_file}")
    print(f"Audio length: {audio_length:.1f} seconds ({audio_length/60:.1f} minutes)")
    print(f"Processing time: {duration:.1f} seconds ({duration/60:.1f} minutes)")
    print(f"Total sentences: {total_sentences}")
    print(f"Individual parts: {session_dir}/")

    print("\n" + "="*60)
    print("HOW TO USE:")
    print("="*60)
    print("1. Edit YOUR_SCRIPT variable in this file")
    print("2. Paste your long script/story")
    print("3. Run: python clone_amit_voice.py")
    print("4. Find output in: Amit_Clone/ directory")
    print("\nTIP: You can paste scripts of any length!")
