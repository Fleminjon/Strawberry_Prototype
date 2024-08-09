from flask import Flask, request, jsonify, render_template
from inference_sdk import InferenceHTTPClient

app = Flask(__name__, template_folder='templates')

# Initialize the Roboflow inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="2sOXJ2RaKgxTqgTrpgWB"
)

MODEL_ID = "strawberry-leaf-disease-jxu2t/2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['file']
    
    # Save the uploaded image temporarily
    image_path = "uploaded_image.jpg"
    image.save(image_path)

    # Perform inference using Roboflow Inference SDK
    result = CLIENT.infer(image_path, model_id=MODEL_ID)
    
    # Process the result
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
