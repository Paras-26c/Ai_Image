import cv2
import re
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

PLATE_REGEX = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{4}$'

def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    return gray

def clean(text):
    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)
    text = text.replace("O", "0").replace("I", "1")
    return text

def extract_number_plate(img):
    img = preprocess(img)
    results = reader.readtext(img)

    for _, text, conf in results:
        text = clean(text)
        if re.match(PLATE_REGEX, text):
            return text, round(conf, 2)

    return "", 0.0
