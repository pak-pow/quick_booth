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
    
    # Check if the request actually contains a file named 'image'
    if 'image' not in request.files:
        return jsonify({"error": "No image sent in request"}), 400
    
    file = request.files['image']
    
    # Check if a file was selected
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
        
    # If the file exists, secure it, rename it, and save it
    if file:
        # Sanitize the filename for safety
        safe_filename = secure_filename(file.filename) # type: ignore
        
        # Generate a unique ID and attach it to the front of the filename
        unique_id = uuid.uuid4().hex
        final_filename = f"{unique_id}_{safe_filename}"
        
        # Create the full path and save the file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], final_filename)
        file.save(filepath)
        
        # Send a success response back to the frontend
        return jsonify({
            "message": "Image successfully uploaded!",
            "filename": final_filename
        }), 200
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)