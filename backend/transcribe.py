import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # You can use "small", "medium", or "large" for better accuracy
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    transcript = transcribe_audio("lecture.mp3")
    print("Transcribed Text:\n", transcript)
