# 📸 Quick Booth

A lightweight, privacy-first photobooth web application. Users can snap multiple photos via their webcam, which are stitched into a classic photobooth strip. To protect user privacy, photos are never permanently saved. Instead, the server generates a temporary QR code so users can instantly download the strip straight to their mobile devices.

## 🛠️ Tech Stack

* **Frontend:** Vanilla HTML5, CSS3, JavaScript
* **Backend:** Python, Flask, Flask-CORS, qrcode
* **Architecture:** Separated Client/Server API model with ephemeral (temporary) file storage.

---

## 📂 Project Structure

```text
quick_booth/
├── backend/                # Python Flask API
│   ├── app.py              # Main server processing & QR generation
│   ├── requirements.txt    # Python dependencies
│   └── temp_uploads/       # Ephemeral storage (auto-cleared)
├── frontend/               # Vanilla JS Client
│   ├── index.html          
│   ├── style.css           
│   └── app.js              
└── docs/                   # Additional documentation

```

---

## 🚀 Local Setup Instructions

### 1. Backend Setup (API Server)

The backend is built with Python and Flask. It handles image reception, QR code generation, and temporary hosting for mobile downloads.

1. Open your terminal and navigate to the backend folder:
```bash
cd backend

```


2. Create and activate a virtual environment:
* **Windows (Git Bash):** `source venv/Scripts/activate`


3. Install the required dependencies:
```bash
pip install -r requirements.txt

```


4. Start the Flask server:
```bash
python app.py

```



### 2. Frontend Setup (Client UI)

1. Open the `frontend` directory in your code editor.
2. Launch the client using the **Live Server** extension in VS Code.

---

## 🔌 API Documentation

### 1. `POST /api/generate-qr`

Receives the completed photobooth strip from the frontend, temporarily stores it, and returns a base64-encoded QR code for the user to scan.

* **URL:** `http://127.0.0.1:5000/api/generate-qr`
* **Method:** `POST`
* **Content-Type:** `multipart/form-data`
* **Body:** `image` (The raw image file)

**Success Response (200 OK):**

```json
{
  "message": "QR Code generated successfully!",
  "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "expires_in": "5 minutes"
}

```

### 2. `GET /api/download/<filename>`

The endpoint encoded inside the QR code. When scanned by a mobile device, it serves the image file for download.

---

## 🤝 Contributors

* **Backend:** [@pak-pow](https://github.com/pak-pow)
* **Frontend:** [@neophiles](https://github.com/neophiles)
