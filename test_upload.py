import requests

# The URL of your local backend
url = 'http://127.0.0.1:5000/api/upload'

# Create a quick dummy image file to test with
with open('fake_photo.jpg', 'wb') as f:
    f.write(b'This is just pretend image data for testing!')

# Open that dummy file and package it up exactly how an HTML form would
with open('fake_photo.jpg', 'rb') as img_file:
    # Notice the key is 'image' - this matches exactly what app.py is looking for!
    files = {'image': img_file}
    
    print(f"Sending request to {url}...")
    
    # Fire the POST request at your server
    response = requests.post(url, files=files)

# Print the server's response
print("Server Response Status Code:", response.status_code)
print("Server Response Data:", response.json())