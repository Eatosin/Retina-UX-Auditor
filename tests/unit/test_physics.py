import numpy as np
import pytest
from src.core.physics.entropy import EntropyEngine
from src.core.physics.contrast import ContrastEngine

@pytest.fixture
def dummy_image():
    """
    Creates a simple synthetic image for testing:
    A 100x100 white square with a black box in the middle.
    """
    # White background (255)
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    # Black box (0)
    img[30:70, 30:70] = 0
    return img

def test_entropy_calculation(dummy_image):
    """
    Verifies that the Entropy Engine returns a valid score between 0-100.
    """
    engine = EntropyEngine()
    score = engine.calculate_clutter_score(dummy_image)
    
    assert isinstance(score, float)
    assert 0 <= score <= 100
    # A simple box should have some clutter (edges), but not 0
    assert score > 0

def test_contrast_calculation(dummy_image):
    """
    Verifies that the Contrast Engine detects the black/white difference.
    """
    engine = ContrastEngine()
    score = engine.calculate_rms_contrast(dummy_image)
    
    assert isinstance(score, float)
    # White vs Black is high contrast, so score should be > 0
    assert score > 0.3

def test_accessibility_verdict():
    """
    Verifies the text output of the verdict logic.
    """
    engine = ContrastEngine()
    
    # Test High Contrast
    assert "Good" in engine.get_accessibility_verdict(0.5)
    
    # Test Low Contrast
    assert "Critical" in engine.get_accessibility_verdict(0.05)
