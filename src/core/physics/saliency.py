import cv2
import numpy as np

class SaliencyEngine:
    """
    Simulates human visual attention using Spectral Residual analysis.
    Generates 'Heatmaps' predicting where users will look first.
    """

    def __init__(self):
        # Initialize the Static Saliency detector (Spectral Residual)
        try:
            self.saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        except AttributeError:
            raise ImportError("OpenCV Contrib not found. Install 'opencv-contrib-python-headless'.")

    def generate_heatmap(self, image: np.ndarray) -> np.ndarray:
        """
        Generates a visual attention heatmap overlaid on the original image.
        """
        if image is None or image.size == 0:
            raise ValueError("Invalid image input")

        # 1. Compute Saliency Map (The Physics)
        # Returns a float array where 1.0 = High Attention, 0.0 = Background
        success, saliency_map = self.saliency.computeSaliency(image)
        
        if not success:
            return image

        # 2. Normalize to 0-255 (Grayscale Image format)
        saliency_map = (saliency_map * 255).astype("uint8")

        # 3. Apply Thermodynamics (Color Mapping)
        # We use COLORMAP_JET (Blue=Cold, Red=Hot)
        heatmap_color = cv2.applyColorMap(saliency_map, cv2.COLORMAP_JET)

        # 4. Fusion (Overlay)
        # Blend: 60% Original Image + 40% Heatmap
        blended = cv2.addWeighted(image, 0.6, heatmap_color, 0.4, 0)

        return blended

    def get_focus_score(self, image: np.ndarray) -> float:
        """
        Returns a 'Focus Score' (0-100). 
        High score = The design forces eyes to a specific spot.
        Low score = The user's eyes wander (Confusion).
        """
        success, saliency_map = self.saliency.computeSaliency(image)
        if not success:
            return 0.0
            
        # Calculate standard deviation of the saliency map.
        # High Std Dev = Strong specific focal points (Good).
        # Low Std Dev = Flat attention (Bad).
        focus_score = np.std(saliency_map) * 100
        
        return round(float(focus_score), 2)