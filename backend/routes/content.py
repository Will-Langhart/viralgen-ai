from flask import Blueprint, request, jsonify
import openai

content_bp = Blueprint('content', __name__)

@content_bp.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get("prompt", "Generate an engaging tweet")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({"generated_content": response["choices"][0]["message"]["content"]})
