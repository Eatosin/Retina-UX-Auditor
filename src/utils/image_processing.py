import cv2
import numpy as np
from typing import Optional, Tuple

def load_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """
    Decodes raw byte stream into an OpenCV BGR image array.
    """
    if not image_bytes:
        raise ValueError("Empty image bytes provided")
        
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Failed to decode image data")
        
    return img

def resize_image(image: np.ndarray, max_width: int = 1024) -> np.ndarray:
    """
    Resizes image to a specific width while maintaining aspect ratio
    to ensure consistent processing speed.
    """
    height, width = image.shape[:2]
    
    if width <= max_width:
        return image
    
    scale = max_width / width
    new_height = int(height * scale)
    
    return cv2.resize(image, (max_width, new_height), interpolation=cv2.INTER_AREA)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts BGR image to Grayscale for edge detection.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
