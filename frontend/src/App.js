import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [transcript, setTranscript] = useState("");

    const uploadFile = async () => {
        const formData = new FormData();
        formData.append("file", file);

        const response = await axios.post("http://127.0.0.1:5000/transcribe", formData);
        setTranscript(response.data.transcript);
    };

    return (
        <div>
            <h1>Auto Lecture Notes</h1>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={uploadFile}>Upload & Transcribe</button>
            <p>{transcript}</p>
        </div>
    );
}

export default App;
