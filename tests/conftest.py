
import pytest
import numpy as np
import cv2

@pytest.fixture
def sample_image():
    # Create a 100x100 white image with a black square
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.rectangle(img, (30, 30), (70, 70), (0, 0, 0), -1)
    return img

@pytest.fixture
def empty_image():
    return np.zeros((100, 100, 3), dtype=np.uint8)
