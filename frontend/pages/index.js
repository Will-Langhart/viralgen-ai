import React, { useState } from 'react';

export default function Home() {
    const [prompt, setPrompt] = useState("");
    const [generatedContent, setGeneratedContent] = useState("");

    // Function to fetch AI-generated content from Flask backend
    const generateContent = async () => {
        const response = await fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt }),
        });

        const data = await response.json();
        setGeneratedContent(data.generated_content);
    };

    return (
        <div style={styles.container}>
            <h1>Welcome to ViralGen AI</h1>

            <div style={styles.inputContainer}>
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Enter a social media topic..."
                    style={styles.input}
                />
                <button onClick={generateContent} style={styles.button}>
                    Generate Post
                </button>
            </div>

            {generatedContent && (
                <div style={styles.result}>
                    <h3>AI-Generated Content:</h3>
                    <p>{generatedContent}</p>
                </div>
            )}
        </div>
    );
}

// Basic inline styles for UI
const styles = {
    container: {
        textAlign: "center",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
    },
    inputContainer: {
        marginTop: "20px",
    },
    input: {
        width: "80%",
        padding: "10px",
        fontSize: "16px",
        borderRadius: "5px",
        border: "1px solid #ddd",
        marginBottom: "10px",
    },
    button: {
        padding: "10px 20px",
        fontSize: "16px",
        backgroundColor: "#4CAF50",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
    },
    result: {
        marginTop: "20px",
        padding: "10px",
        backgroundColor: "#f9f9f9",
        borderRadius: "5px",
        textAlign: "left",
    },
};
