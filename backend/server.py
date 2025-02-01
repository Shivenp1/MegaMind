from flask import Flask, request, jsonify
from transcribe import transcribe_audio
from nlp_processing import extract_keywords
from mindmap_generator import create_mind_map

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["file"]
    file_path = "uploaded_audio.mp3"
    file.save(file_path)
    
    text = transcribe_audio(file_path)
    keywords = extract_keywords(text)
    
    return jsonify({"transcript": text, "keywords": keywords})

if __name__ == "__main__":
    app.run(debug=True)
