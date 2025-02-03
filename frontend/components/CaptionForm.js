import React, { useState } from 'react';

export default function CaptionForm() {
    const [prompt, setPrompt] = useState("");
    const [caption, setCaption] = useState("");

    const generateCaption = async () => {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });
        const data = await response.json();
        setCaption(data.generated_content);
    };

    return (
        <div>
            <h1>Generate AI Captions</h1>
            <input type="text" value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Enter prompt" />
            <button onClick={generateCaption}>Generate</button>
            <p>{caption}</p>
        </div>
    );
}
