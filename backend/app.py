from flask import Flask, request, jsonify, send_from_directory
import os
import openai
import logging

# Set up Flask app
app = Flask(__name__, static_folder=os.path.abspath("build"))

# Logging setup
logging.basicConfig(level=logging.INFO)

# Load OpenAI API Key from Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# Serve React frontend
@app.route("/")
def serve_react_index():
    if not os.path.exists(os.path.join(app.static_folder, "index.html")):
        logging.error("Error: React build not found.")
        return jsonify({"error": "Frontend not found. Make sure the React build exists."}), 500
    return send_from_directory(app.static_folder, "index.html")

# Serve static files (CSS, JS, Images)
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# AI Content Generation Endpoint
@app.route("/generate", methods=["POST"])
def generate_content():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        logging.info(f"Generating AI content for prompt: {prompt}")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI content generator."},
                      {"role": "user", "content": f"Generate a viral social media post about: {prompt}"}]
        )

        generated_text = response["choices"][0]["message"]["content"].strip()
        logging.info(f"AI Generated Content: {generated_text}")

        return jsonify({"generated_content": generated_text})

    except openai.OpenAIError as oe:
        logging.error(f"OpenAI API error: {oe}")
        return jsonify({"error": "AI service unavailable, try again later."}), 503

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
