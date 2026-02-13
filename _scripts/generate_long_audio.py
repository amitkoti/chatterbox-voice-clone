"""
Long Audio Generator
Automatically splits long text into chunks and generates complete audio
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
    # Split on sentence endings
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Clean up
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def generate_long_audio(text, voice_reference, output_name="long_audio", save_parts=True):
    """
    Generate long audio from text using voice cloning

    Args:
        text: Long text to convert to speech
        voice_reference: Path to reference audio file
        output_name: Name for output files
        save_parts: Whether to save individual sentence files
    """

    print("="*60)
    print("LONG AUDIO GENERATOR")
    print("="*60)

    # Check if reference exists
    if not os.path.exists(voice_reference):
        print(f"ERROR: Cannot find reference audio: {voice_reference}")
        return None

    # Split text
    sentences = split_into_sentences(text)
    total_sentences = len(sentences)

    print(f"\nText split into {total_sentences} sentences")
    print(f"Reference voice: {voice_reference}")
    print(f"Estimated time: ~{total_sentences * 10} seconds on CPU")
    print("\nStarting generation...")
    print("-" * 60)

    # Load model
    print("\nLoading Chatterbox model...")
    tts = ChatterboxTTS.from_pretrained(device="cpu")
    print("Model loaded!\n")

    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{output_name}_{timestamp}"
    if save_parts:
        os.makedirs(output_dir, exist_ok=True)

    # Generate audio for each sentence
    audio_chunks = []
    start_time = datetime.now()

    for i, sentence in enumerate(sentences, 1):
        # Show progress
        progress = f"[{i}/{total_sentences}]"
        preview = sentence[:60] + "..." if len(sentence) > 60 else sentence
        print(f"{progress} {preview}")

        # Generate audio
        audio = tts.generate(sentence, audio_prompt_path=voice_reference)
        audio_np = audio.cpu().numpy().squeeze()
        audio_chunks.append(audio_np)

        # Optionally save individual parts
        if save_parts:
            part_file = os.path.join(output_dir, f"part_{i:04d}.wav")
            sf.write(part_file, audio_np, 24000, subtype='PCM_16')

    # Calculate time taken
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("\n" + "-" * 60)
    print("Combining audio chunks...")

    # Combine all chunks
    combined_audio = np.concatenate(audio_chunks)

    # Save combined audio
    output_file = f"{output_name}_{timestamp}_complete.wav"
    sf.write(output_file, combined_audio, 24000, subtype='PCM_16')

    # Calculate audio length
    audio_length = len(combined_audio) / 24000  # seconds

    print("\n" + "="*60)
    print("SUCCESS!")
    print("="*60)
    print(f"Generated: {output_file}")
    print(f"Audio length: {audio_length:.1f} seconds ({audio_length/60:.1f} minutes)")
    print(f"Processing time: {duration:.1f} seconds ({duration/60:.1f} minutes)")
    print(f"Sentences: {total_sentences}")
    if save_parts:
        print(f"Individual parts saved in: {output_dir}/")

    return output_file

# ============================================
# CONFIGURATION
# ============================================

# Choose which voice to use:
VOICE_REFERENCE = "_reference_audio/Saanvi_Voice_Clone.wav"  # or "_reference_audio/audio_sample.wav"

# Your long text here (or read from file):
LONG_TEXT = """
Hello everyone! This is a demonstration of long audio generation.

I can speak for as long as you need me to. Whether it's a short story,
a long article, or even an entire book chapter.

The system automatically splits the text into sentences and generates
each one individually. Then it combines them all into a single audio file.

This approach ensures consistent quality throughout the entire recording.
Each sentence is generated with the same voice characteristics.

You can use this for many purposes. Create audiobooks, narrate stories,
make educational content, or generate personalized messages.

The possibilities are endless. And the best part? The voice sounds
natural and expressive throughout the entire recording.

Thank you for listening to this demonstration!
"""

# Alternative: Read from a text file
# with open("my_story.txt", "r", encoding="utf-8") as f:
#     LONG_TEXT = f.read()

# ============================================
# GENERATE
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("LONG AUDIO GENERATOR - Universal Voice Clone Tool")
    print("="*60)

    # Parse command line arguments
    if len(sys.argv) >= 3:
        # Command line mode: python generate_long_audio.py <voice> <text_file>
        voice_choice = sys.argv[1].lower()
        text_file = sys.argv[2]

        # Select voice reference
        if voice_choice in ["amit", "a"]:
            voice_ref = "_reference_audio/audio_sample.wav"
            output_prefix = "amit"
        elif voice_choice in ["saanvi", "s"]:
            voice_ref = "_reference_audio/Saanvi_Voice_Clone.wav"
            output_prefix = "saanvi"
        else:
            print(f"\nERROR: Unknown voice '{voice_choice}'")
            print("\nUsage: python generate_long_audio.py <voice> <text_file>")
            print("\nVoice options:")
            print("  amit (or a)   - Use Amit's voice")
            print("  saanvi (or s) - Use Saanvi's voice")
            print("\nExample:")
            print("  python generate_long_audio.py amit my_script.txt")
            print("  python generate_long_audio.py saanvi story.txt")
            exit(1)

        # Read text file
        if not os.path.exists(text_file):
            print(f"\nERROR: Text file not found: {text_file}")
            exit(1)

        print(f"\nVoice: {voice_choice.upper()}")
        print(f"Text file: {text_file}")
        print(f"Reference: {voice_ref}")

        with open(text_file, 'r', encoding='utf-8') as f:
            text_content = f.read()

        # Generate audio
        output_file = generate_long_audio(
            text=text_content,
            voice_reference=voice_ref,
            output_name=output_prefix,
            save_parts=True
        )

        if output_file:
            print(f"\n{'='*60}")
            print("DONE! Play your audio:")
            print(f"  {output_file}")

    else:
        # Interactive/Help mode
        print("\nUSAGE:")
        print("="*60)
        print("\nCommand line (RECOMMENDED):")
        print("  python generate_long_audio.py <voice> <text_file>")
        print("\nExamples:")
        print("  python generate_long_audio.py amit my_script.txt")
        print("  python generate_long_audio.py saanvi story.txt")
        print("\nVoice options:")
        print("  amit (or a)   - Amit's voice")
        print("  saanvi (or s) - Saanvi's voice")
        print("\n" + "="*60)
        print("ALTERNATIVE: Edit this script")
        print("="*60)
        print("1. Change VOICE_REFERENCE and LONG_TEXT variables")
        print("2. Run: python generate_long_audio.py")

        # Try to use the hardcoded values
        if os.path.exists(VOICE_REFERENCE):
            print("\n" + "-"*60)
            print(f"Using hardcoded values:")
            print(f"  Voice: {VOICE_REFERENCE}")
            choice = input("\nGenerate audio with these settings? (y/n): ").lower()

            if choice == 'y':
                output_file = generate_long_audio(
                    text=LONG_TEXT,
                    voice_reference=VOICE_REFERENCE,
                    output_name="generated_audio",
                    save_parts=True
                )
                if output_file:
                    print(f"\nDONE! Play: {output_file}")
