import cv2
import numpy as np

def classify_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 150)
    edge_ratio = np.sum(edges > 0) / edges.size

    # dashboard has lots of text/edges
    if edge_ratio > 0.15:
        return "dashboard"
    return "vehicle"
