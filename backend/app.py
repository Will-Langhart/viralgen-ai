from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the path to the frontend directory
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), "pages")

@app.route('/')
def serve_react_index():
    """Serve the index.js React file from the backend/pages directory."""
    return send_from_directory(FRONTEND_PATH, "index.js")

if __name__ == '__main__':
    app.run(debug=True)
