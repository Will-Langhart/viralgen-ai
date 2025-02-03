from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Define the correct path to the frontend directory
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), "../frontend/pages")

@app.route('/')
def serve_react_index():
    """Serve the index.js React file from the frontend/pages directory."""
    index_path = os.path.join(FRONTEND_PATH, "index.js")

    if os.path.exists(index_path):
        return send_from_directory(FRONTEND_PATH, "index.js")
    else:
        return jsonify({"error": "index.js not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
