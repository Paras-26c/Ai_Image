import cv2
import pytesseract
import re

def extract_odometer(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    roi = gray[int(h*0.6):int(h*0.9), int(w*0.3):int(w*0.7)]
    roi = cv2.resize(roi, None, fx=2, fy=2)

    text = pytesseract.image_to_string(
        roi,
        config="--psm 7 -c tessedit_char_whitelist=0123456789"
    )

    digits = re.sub(r'\D', '', text)
    if len(digits) >= 4:
        return int(digits), 0.9

    return None, 0.0
