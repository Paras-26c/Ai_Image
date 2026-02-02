import cv2
from app.services.image_type import classify_image
from app.services.vehicle_detector import detect_vehicle
from app.services.number_plate import extract_number_plate
from app.services.odometer import extract_odometer


def inspect_images(image_paths):
    result = {
        "vehicle_detected": False,
        "vehicle_type": None,
        "number_plate": "",
        "plate_confidence": 0.0,
        "odometer": None,
        "interior": False,
        "exterior": False,
        "confidence": 0.0
    }

    for path in image_paths:
        img = cv2.imread(path)
        if img is None:
            continue

        img_type = classify_image(img)

        # 🔹 DASHBOARD IMAGE → ODOMETER
        if img_type == "dashboard":
            odo, conf = extract_odometer(img)
            if odo:
                result["odometer"] = odo
                result["confidence"] = max(result["confidence"], conf)
            continue

        # 🔹 VEHICLE IMAGE
        detected, v_type, v_conf = detect_vehicle(path)  # ✅ FIX HERE
        if not detected:
            continue

        result["vehicle_detected"] = True
        result["vehicle_type"] = v_type
        result["exterior"] = True
        result["confidence"] = max(result["confidence"], v_conf)

        # 🔹 NUMBER PLATE OCR
        plate, p_conf = extract_number_plate(img)
        if plate:
            result["number_plate"] = plate
            result["plate_confidence"] = p_conf

    return result
