from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder='templates')

# Replace with your actual Roboflow API details
ROBOFLOW_API_KEY = "2sOXJ2RaKgxTqgTrpgWB"
ROBOFLOW_MODEL = "strawberry-leaf-disease-jxu2"
ROBOFLOW_VERSION = "v2"
ROBOFLOW_API_URL = "https://universe.roboflow.com/strawberry-leaf-disease/strawberry-leaf-disease-jxu2t"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['file']

    # Send image to Roboflow API
    response = requests.post(
        ROBOFLOW_API_URL,
        files={"file": image},
        params={"api_key": ROBOFLOW_API_KEY}
    )
    
    # Process the response
    if response.status_code == 500:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to get a response from Roboflow."}), 500

if __name__ == '__main__':
    app.run(debug=True)
