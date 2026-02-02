import cv2
import numpy as np
import os

def load_image(input_data):
    """
    Accepts:
    - file bytes (from upload)
    - file path (string)
    """
    # Case 1: file path
    if isinstance(input_data, str) and os.path.exists(input_data):
        return cv2.imread(input_data)

    # Case 2: bytes
    if isinstance(input_data, (bytes, bytearray)):
        image = np.frombuffer(input_data, np.uint8)
        return cv2.imdecode(image, cv2.IMREAD_COLOR)

    raise ValueError("Unsupported image input type")


def enhance_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    contrast = clahe.apply(gray)

    sharp = cv2.GaussianBlur(contrast, (0, 0), 3)
    sharp = cv2.addWeighted(contrast, 1.5, sharp, -0.5, 0)

    return sharp

def resize_up(image, scale=2):
    return cv2.resize(
        image,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_CUBIC
    )
