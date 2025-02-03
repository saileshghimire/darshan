# Nepali Sign Language Alphabet Detection API

A Flask-based REST API for detecting Nepali alphabet sign language gestures using YOLOv8 object detection model.

## Features

- Real-time sign language detection using YOLOv8
- Accepts base64 encoded images as input
- Returns JSON response with detected character and confidence
- Easy integration with web/mobile applications

## Prerequisites

- Python 3.8+
- pip package manager
- YOLOv8 model weights file (`best.pt`)
- Basic understanding of REST APIs

## Installation

1. Clone the repository:
```bash
git clone git@github.com:saileshghimire/major-backend-working-api.git

```
2. Intall requirement Dependicies
```bash
pip install -r requirements.txt
```
3. Run project
``` bash
python app.py
```
The API will start running on http://0.0.0.0:5000
### Request
Accepts a base64-encoded image and returns the detected Nepali alphabet and its confidence score.

API Endpoints "/perdict"
```
{
    "image": "base64_encoded_image_string"
}
```
### Response
```
{
    "success": true,
    "results": "Detected_Alphabet",
    "Probability": 0.95
}
```

### Error
```
{
    "success": false,
    "error": "Error message"
}
```



   
