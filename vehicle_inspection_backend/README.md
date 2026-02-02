# AI Image Detection System - Vehicle Inspection Backend

This is a FastAPI-based backend service for AI-powered vehicle inspection using image analysis. It detects vehicles, extracts number plates, reads odometer values, and assesses image quality.

## Features

- **Vehicle Detection**: Identifies vehicle types (car, bike, bus, truck) using YOLOv8
- **Number Plate Extraction**: Uses OCR to extract license plate numbers
- **Odometer Reading**: Extracts mileage from dashboard images
- **Image Quality Assessment**: Checks for blurriness
- **Interior/Exterior Classification**: Determines if image is interior or exterior view

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vehicle_inspection_backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download YOLO models (yolov8s.pt and yolov8n.pt should be in the root directory)

## Usage

Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

### POST /api/v1/image/inspect

Upload an image for inspection.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `file` (image file)

**Response:**
```json
{
  "image_id": "uuid",
  "result": {
    "vehicle_present": true,
    "vehicle_type": "car",
    "image_view": "exterior",
    "number_plate": "AB12CD3456",
    "odometer": 12345,
    "confidence": 0.85,
    "image_quality": "clear"
  }
}
```

## Project Structure

```
vehicle_inspection_backend/
├── app/
│   ├── main.py              # FastAPI app
│   ├── api/
│   │   └── routes.py        # API routes
│   ├── services/
│   │   ├── inspector.py     # Main inspection logic
│   │   ├── vehicle_detector.py
│   │   ├── number_plate.py
│   │   ├── odometer.py
│   │   ├── image_quality.py
│   │   ├── interior_exterior.py
│   │   └── image_type.py
│   └── utils/
│       └── image_utils.py   # Image processing utilities
├── requirements.txt
├── yolov8s.pt
└── yolov8n.pt
```

## Dependencies

- FastAPI: Web framework
- Uvicorn: ASGI server
- OpenCV: Image processing
- EasyOCR: OCR for text extraction
- Ultralytics YOLO: Object detection
- NumPy: Numerical operations
- Pillow: Image handling
- Python-multipart: File uploads

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License
