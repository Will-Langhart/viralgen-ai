from flask import Flask, request, jsonify, send_from_directory
import os
import openai

app = Flask(__name__, static_folder="build", static_url_path="/")

# Serve React Frontend
@app.route('/')
def serve_react_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# AI Content Generation Endpoint
@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get("prompt", "")

    # AI Integration (Replace with your OpenAI API key)
    openai.api_key = "YOUR_OPENAI_API_KEY"

    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Generate a viral social media post about: {prompt}",
            max_tokens=100
        )
        return jsonify({"generated_content": response["choices"][0]["text"]})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
