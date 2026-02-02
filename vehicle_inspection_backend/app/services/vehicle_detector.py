from ultralytics import YOLO
import cv2

vehicle_model = YOLO("yolov8n.pt")  # root folder me hona chahiye

CLASS_MAP = {
    "car": "car",
    "motorcycle": "two_wheeler",
    "bus": "bus",
    "truck": "truck"
}

def detect_vehicle(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return False, None, 0.0

    results = vehicle_model(img, conf=0.4)

    best_conf = 0.0
    best_type = None

    for r in results:
        for box in r.boxes:
            label = r.names[int(box.cls[0])]
            conf = float(box.conf[0])
            if label in CLASS_MAP and conf > best_conf:
                best_conf = conf
                best_type = CLASS_MAP[label]

    if best_type:
        return True, best_type, round(best_conf, 2)

    return False, None, 0.0
