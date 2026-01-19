import cv2
import numpy as np
from src.utils.image_processing import convert_to_grayscale

class ContrastEngine:
    """
    Analyzes Root Mean Square (RMS) Contrast to determine visual accessibility.
    """

    def calculate_rms_contrast(self, image: np.ndarray) -> float:
        """
        Calculates global RMS contrast of the image.
        Returns a value typically between 0.0 (Gray) and 1.0 (High Contrast).
        """
        if image is None or image.size == 0:
            return 0.0

        gray = convert_to_grayscale(image)
        
        # Normalize pixel values to 0-1 range
        img_norm = gray.astype(float) / 255.0
        
        # RMS Contrast = Standard Deviation of pixel intensities
        contrast = np.std(img_norm)
        
        return round(float(contrast), 4)

    def get_accessibility_verdict(self, contrast_score: float) -> str:
        """
        Returns a basic verdict based on global contrast levels.
        """
        # RMS thresholds derived from standard web accessibility studies
        if contrast_score < 0.1:
            return "Critical: Very Low Contrast"
        elif contrast_score < 0.2:
            return "Warning: Low Contrast"
        elif contrast_score > 0.4:
            return "Good: High Contrast"
        else:
            return "Moderate: Acceptable"
