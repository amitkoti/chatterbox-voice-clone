# Chatterbox Voice Cloning Example

# Workaround for missing PerthImplicitWatermarker
import perth
if perth.PerthImplicitWatermarker is None:
    print("Note: Using DummyWatermarker (Perth watermarker not available)")
    perth.PerthImplicitWatermarker = perth.DummyWatermarker

from chatterbox import ChatterboxTTS
import soundfile as sf
import numpy as np

# Load the model
print("Loading Chatterbox model...")
tts_model = ChatterboxTTS.from_pretrained(device="cpu")

# ============================================
# METHOD 1: Clone voice from audio file
# ============================================
def clone_voice_from_file(reference_audio_path, text_to_synthesize):
    """
    Clone a voice from a reference audio file.

    Args:
        reference_audio_path: Path to the reference audio file (WAV, MP3, etc.)
        text_to_synthesize: Text you want the cloned voice to say
    """
    print(f"\nCloning voice from: {reference_audio_path}")
    print(f"Text to synthesize: {text_to_synthesize}")

    # Prepare the voice conditionals from the reference audio
    conditionals = tts_model.prepare_conditionals(reference_audio_path)

    # Generate audio with the cloned voice
    print("Generating audio with cloned voice...")
    audio = tts_model.generate(text_to_synthesize, conditionals=conditionals)

    # Convert to numpy and save
    if hasattr(audio, 'cpu'):
        audio = audio.cpu().numpy()
    if len(audio.shape) > 1:
        audio = audio.squeeze()

    output_path = "cloned_voice_output.wav"
    sf.write(output_path, audio, 24000, subtype='PCM_16')
    print(f"SUCCESS: Cloned voice saved to '{output_path}'")

    return output_path


# ============================================
# METHOD 2: Use built-in voices
# ============================================
def use_builtin_voice(text_to_synthesize):
    """
    Use Chatterbox's built-in default voice.
    """
    print(f"\nUsing built-in voice")
    print(f"Text to synthesize: {text_to_synthesize}")

    # Generate with default voice (no conditionals)
    print("Generating audio with built-in voice...")
    audio = tts_model.generate(text_to_synthesize)

    # Convert to numpy and save
    if hasattr(audio, 'cpu'):
        audio = audio.cpu().numpy()
    if len(audio.shape) > 1:
        audio = audio.squeeze()

    output_path = "builtin_voice_output.wav"
    sf.write(output_path, audio, 24000, subtype='PCM_16')
    print(f"SUCCESS: Audio saved to '{output_path}'")

    return output_path


# ============================================
# EXAMPLE USAGE
# ============================================
if __name__ == "__main__":
    # Example 1: Use built-in voice
    print("\n" + "="*60)
    print("EXAMPLE 1: Using built-in voice")
    print("="*60)
    use_builtin_voice("Hello, this is a test of the built-in voice.")

    # Example 2: Clone a voice (you need to provide your own reference audio)
    print("\n" + "="*60)
    print("EXAMPLE 2: Voice cloning from reference audio")
    print("="*60)

    # IMPORTANT: Replace this path with your own reference audio file
    reference_audio = "path/to/your/reference_audio.wav"

    # Check if reference audio exists
    import os
    if os.path.exists(reference_audio):
        clone_voice_from_file(
            reference_audio_path=reference_audio,
            text_to_synthesize="This is my cloned voice speaking. Amazing, isn't it?"
        )
    else:
        print(f"\nTo clone a voice, please:")
        print("1. Prepare a clean audio recording (10-30 seconds)")
        print("2. Save it as a WAV file")
        print("3. Update the 'reference_audio' variable with the file path")
        print("4. Run this script again")
        print("\nFor now, I'll just use the built-in voice.")
