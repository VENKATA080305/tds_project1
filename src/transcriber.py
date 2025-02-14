import whisper

def transcribe_audio(audio_path):
    """Transcribe speech from an MP3 file using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]
