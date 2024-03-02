from flask import Flask, request, jsonify, Response
import ultralytics
from ultralytics import YOLO
from PIL import Image
import io
import base64

app = Flask(__name__)

# Initialize your YOLOv8 model here
try:
    yolo_model = YOLO("best.pt")
    print("YOLOv8 model initialized successfully")
except Exception as e:
    print(f"Error initializing YOLOv8 model: {e}")
    yolo_model = None

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get image data from the JSON request
        json_data = request.get_json()
        base64_image = json_data['image']
        
        # Convert base64 image to bytes
        image_bytes = base64.b64decode(base64_image)
        
        # Open image from bytes
        image = Image.open(io.BytesIO(image_bytes))

        # Perform YOLOv8 inference
        results = yolo_model.predict(image)

        # Process results as needed
        # ...
        result = results[0]
        box = result.boxes[0]

        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        class_id = result.names[box.cls[0].item()]
        conf = round(box.conf[0].item(), 2)
        

        return jsonify({"success": True, 'results': class_id, 'Probability': conf})
    except Exception as e:
        return jsonify({"success": False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
