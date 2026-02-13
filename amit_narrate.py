"""
Amit's Voice - Quick Narration Tool
Read from text file or command line
"""

import perth
if perth.PerthImplicitWatermarker is None:
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import numpy as np
import re
import os
import sys
from datetime import datetime

def split_into_sentences(text):
    """Split text into sentences"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def generate_audio(text, reference_audio="_reference_audio/audio_sample.wav", output_dir="Amit_Clone"):
    """Generate audio from text using Amit's voice"""

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Check reference
    if not os.path.exists(reference_audio):
        print(f"ERROR: Cannot find {reference_audio}")
        return None

    # Split text
    sentences = split_into_sentences(text)
    if not sentences:
        print("ERROR: No text provided!")
        return None

    print(f"Generating {len(sentences)} sentences with Amit's voice...")

    # Load model
    tts = ChatterboxTTS.from_pretrained(device="cpu")

    # Generate
    audio_chunks = []
    for i, sentence in enumerate(sentences, 1):
        print(f"[{i}/{len(sentences)}] {sentence[:50]}...")
        audio = tts.generate(sentence, audio_prompt_path=reference_audio)
        audio_chunks.append(audio.cpu().numpy().squeeze())

    # Combine
    combined = np.concatenate(audio_chunks)

    # Save
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"amit_{timestamp}.wav")
    sf.write(output_file, combined, 24000, subtype='PCM_16')

    duration = len(combined) / 24000
    print(f"\nSUCCESS! Saved: {output_file}")
    print(f"Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")

    return output_file

# ============================================
# USAGE
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("AMIT'S VOICE - NARRATION TOOL")
    print("="*60)

    # Method 1: From text file
    if len(sys.argv) > 1:
        script_file = sys.argv[1]
        if os.path.exists(script_file):
            print(f"\nReading script from: {script_file}")
            with open(script_file, 'r', encoding='utf-8') as f:
                script = f.read()
            generate_audio(script)
        else:
            print(f"\nERROR: File not found: {script_file}")
            print("\nUsage: python amit_narrate.py script.txt")

    # Method 2: Interactive
    else:
        print("\n3 ways to use this tool:")
        print("\n1. From text file:")
        print("   python amit_narrate.py your_script.txt")

        print("\n2. Create a text file called 'amit_script.txt'")
        print("   Put your text in it, then run:")
        print("   python amit_narrate.py amit_script.txt")

        print("\n3. Edit YOUR_SCRIPT in clone_amit_voice.py")
        print("   Then run: python clone_amit_voice.py")

        print("\n" + "-"*60)

        # Check for default script file
        if os.path.exists("amit_script.txt"):
            print("\nFound 'amit_script.txt'!")
            choice = input("Generate audio from this file? (y/n): ").lower()
            if choice == 'y':
                with open("amit_script.txt", 'r', encoding='utf-8') as f:
                    script = f.read()
                generate_audio(script)
        else:
            print("\nNo script file found.")
            print("Create 'amit_script.txt' with your text and run this again.")
