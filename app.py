from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

# enable CORS
CORS(app)

# Setup Upload Folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/status', methods=['GET']) # type: ignore

def status():
    return jsonify({"message": "Quick Booth Python Backend is up and running"})

# Image Upload Route
@app.route('/api/upload', methods=['POST']) #type: ignore
def upload_image():
    # 1. Check if the request actually contains a file named 'image'
    if 'image' not in request.files:
        return jsonify({"error": "No image sent in request"}), 400