from flask import Flask, request, jsonify, send_from_directory
import os
import openai
import logging

# Initialize Flask app with React frontend serving
app = Flask(__name__, static_folder="build", static_url_path="/")

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO)

# Load OpenAI API Key from Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your_default_api_key_here")

# Serve React Frontend
@app.route('/')
def serve_react_index():
    try:
        return send_from_directory(app.static_folder, "index.html")
    except Exception as e:
        logging.error(f"Error serving React index.html: {e}")
        return jsonify({"error": "Frontend not found. Make sure the React build exists."}), 500

# Serve Static Files (JS, CSS, Images)
@app.route('/<path:path>')
def serve_static_files(path):
    try:
        return send_from_directory(app.static_folder, path)
    except Exception as e:
        logging.error(f"Error serving static file '{path}': {e}")
        return jsonify({"error": f"Static file '{path}' not found."}), 404

# AI Content Generation Endpoint
@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        logging.info(f"Generating AI content for prompt: {prompt}")

        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Generate a viral social media post about: {prompt}",
            max_tokens=100
        )

        generated_text = response["choices"][0]["text"].strip()
        logging.info(f"AI Generated Content: {generated_text}")

        return jsonify({"generated_content": generated_text})

    except openai.error.OpenAIError as oe:
        logging.error(f"OpenAI API error: {oe}")
        return jsonify({"error": "AI service unavailable, try again later."}), 503

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
