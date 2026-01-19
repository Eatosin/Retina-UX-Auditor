import cv2
import numpy as np
from src.utils.image_processing import convert_to_grayscale

class EntropyEngine:
    """
    Analyzes Visual Entropy (Clutter) using Edge Density algorithms.
    High edge density correlates with high cognitive load.
    """
    
    # Standard thresholds for UI edge detection
    LOWER_THRESH = 100
    UPPER_THRESH = 200

    def calculate_clutter_score(self, image: np.ndarray) -> float:
        """
        Calculates the density of visual edges in the UI.
        Returns a normalized score 0-100 (Higher = More Cluttered).
        """
        if image is None or image.size == 0:
            return 0.0

        gray = convert_to_grayscale(image)
        
        # Detect structural edges
        edges = cv2.Canny(gray, self.LOWER_THRESH, self.UPPER_THRESH)
        
        height, width = edges.shape
        total_pixels = height * width
        
        if total_pixels == 0:
            return 0.0

        # Count white pixels (edges)
        edge_pixels = np.count_nonzero(edges)
        
        # Calculate raw density
        density = (edge_pixels / total_pixels) * 100
        
        # Normalize: UI clutter typically caps around 20% raw edge density.
        # Scaling factor of 5 maps 0-20% density to 0-100 score.
        normalized_score = min(100.0, density * 5.0)
        
        return round(normalized_score, 2)
