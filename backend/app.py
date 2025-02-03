# ViralGen AI - AI-Powered Social Media Content Generator

## Backend (Django/Flask)

### app.py (Main Application File)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ViralGen AI!"

if __name__ == '__main__':
    app.run(debug=True)
