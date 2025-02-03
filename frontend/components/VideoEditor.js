import React, { useState } from 'react';

export default function VideoEditor() {
    const [topic, setTopic] = useState("");
    const [script, setScript] = useState("");

    const generateScript = () => {
        setScript(`Script for ${topic}: AI-powered video introduction...`);
    };

    return (
        <div>
            <h1>AI Video Script Generator</h1>
            <input type="text" value={topic} onChange={(e) => setTopic(e.target.value)} placeholder="Enter video topic" />
            <button onClick={generateScript}>Generate Script</button>
            <pre>{script}</pre>
        </div>
    );
}
