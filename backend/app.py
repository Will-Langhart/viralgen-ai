from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="build", static_url_path="/")

@app.route('/')
def serve_react_index():
    """Serve the React frontend index.html"""
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_static_files(path):
    """Serve static assets from the React build folder"""
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
