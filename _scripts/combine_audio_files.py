"""
Audio File Combiner
Combines multiple WAV files into a single file
"""

import soundfile as sf
import numpy as np
import os
from pathlib import Path

def combine_audio_files(file_list, output_name="combined_audio.wav", add_silence=False, silence_ms=500):
    """
    Combine multiple audio files into one

    Args:
        file_list: List of audio file paths to combine
        output_name: Name for output file
        add_silence: Whether to add silence between files
        silence_ms: Milliseconds of silence to add between files
    """

    print("="*60)
    print("AUDIO FILE COMBINER")
    print("="*60)

    audio_chunks = []
    total_duration = 0

    print(f"\nCombining {len(file_list)} files...")
    print("-" * 60)

    for i, file_path in enumerate(file_list, 1):
        if not os.path.exists(file_path):
            print(f"⚠ Skipping {file_path} (not found)")
            continue

        # Read audio file
        audio, sr = sf.read(file_path)

        # Handle different sample rates
        if sr != 24000:
            print(f"⚠ Warning: {file_path} has sample rate {sr}Hz (expected 24000Hz)")

        duration = len(audio) / sr
        total_duration += duration

        print(f"[{i}/{len(file_list)}] {Path(file_path).name} ({duration:.1f}s)")

        audio_chunks.append(audio)

        # Add silence between files if requested
        if add_silence and i < len(file_list):
            silence_samples = int(sr * silence_ms / 1000)
            silence = np.zeros(silence_samples)
            audio_chunks.append(silence)
            total_duration += silence_ms / 1000

    if not audio_chunks:
        print("ERROR: No valid audio files found!")
        return None

    # Combine all chunks
    print("\nCombining audio...")
    combined = np.concatenate(audio_chunks)

    # Save
    sf.write(output_name, combined, 24000, subtype='PCM_16')

    print("\n" + "="*60)
    print("SUCCESS!")
    print("="*60)
    print(f"Output: {output_name}")
    print(f"Total duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
    print(f"Files combined: {len(file_list)}")

    return output_name


# ============================================
# USAGE EXAMPLES
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("AUDIO COMBINER - USAGE")
    print("="*60)
    print("\nChoose how you want to combine files:\n")

    # Example 1: Combine specific files
    print("1. Combine specific files:")
    print("""
    files = [
        "cloned_output_1.wav",
        "cloned_output_2.wav",
        "cloned_output_3.wav"
    ]
    combine_audio_files(files, "my_combined_audio.wav")
    """)

    # Example 2: Combine all files from a directory
    print("\n2. Combine all files from Saanvi_Clone directory:")
    print("""
    from pathlib import Path
    files = sorted(Path("Saanvi_Clone").glob("*.wav"))
    files = [str(f) for f in files]
    combine_audio_files(files, "saanvi_complete.wav")
    """)

    # Example 3: With silence between files
    print("\n3. With 1 second silence between parts:")
    print("""
    combine_audio_files(
        files,
        "my_audio.wav",
        add_silence=True,
        silence_ms=1000
    )
    """)

    print("\n" + "-"*60)
    print("QUICK START:")
    print("-"*60)

    # Check what directories exist
    print("\nAvailable audio to combine:")

    # Check for Saanvi_Clone directory
    if os.path.exists("Saanvi_Clone"):
        saanvi_files = sorted(Path("Saanvi_Clone").glob("*.wav"))
        if saanvi_files:
            print(f"\n✓ Saanvi_Clone/ ({len(saanvi_files)} files)")

            choice = input("\nCombine Saanvi's audio files? (y/n): ").lower()
            if choice == 'y':
                files = [str(f) for f in saanvi_files]
                combine_audio_files(
                    files,
                    "saanvi_combined_complete.wav",
                    add_silence=True,
                    silence_ms=500
                )
                print("\n✓ Done! Check: saanvi_combined_complete.wav")
                exit(0)

    # Check for your cloned outputs
    your_files = list(Path(".").glob("cloned_output_*.wav"))
    if your_files:
        your_files = sorted(your_files)
        print(f"\n✓ Your cloned audio files ({len(your_files)} files)")

        choice = input("\nCombine your audio files? (y/n): ").lower()
        if choice == 'y':
            files = [str(f) for f in your_files]
            combine_audio_files(
                files,
                "my_voice_combined.wav",
                add_silence=True,
                silence_ms=500
            )
            print("\n✓ Done! Check: my_voice_combined.wav")
            exit(0)

    print("\n" + "-"*60)
    print("To use this script:")
    print("1. Edit the file list in the script")
    print("2. Or use the examples above in your own Python code")
    print("-"*60)
