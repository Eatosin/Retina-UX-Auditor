import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from src.utils.prompt_loader import load_prompt_config

# Load Env
load_dotenv()
logger = logging.getLogger(__name__)

class DesignCritic:
    """
    The Intelligence Layer.
    Uses Multimodal LLMs (Gemini 3.0/2.5) to analyze UI/UX based on Physics Metrics.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")
        genai.configure(api_key=api_key)
        
        # Load SOTA Prompt Strategy
        self.prompt_config = load_prompt_config("ux_auditor")

    def _get_model(self):
        """
        Smart Router: Tries Bleeding Edge (3.0) first, falls back to Stable (2.5).
        """
        try:
            return genai.GenerativeModel('models/gemini-3-flash-preview')
        except:
            logger.warning("Gemini 3.0 unavailable, switching to 2.5.")
            return genai.GenerativeModel('models/gemini-2.5-flash')

    def analyze(self, image_bytes: bytes, metrics: dict) -> str:
        """
        Generates a UX Audit based on Visual Physics using externalized prompts.
        """
        model = self._get_model()
        
        # 1. Hydrate the Prompt with Dynamic Metrics
        # Use str() to ensure safe fallback if metrics are missing
        context = self.prompt_config["context_instruction"].format(
            clutter_score=metrics.get('clutter_score', 'N/A'),
            contrast_verdict=metrics.get('contrast_verdict', 'N/A'),
            focus_score=metrics.get('focus_score', 'N/A')
        )
        
        # 2. Assemble the Full Chain of Thought
        full_prompt = [
            self.prompt_config["role"],
            context,
            self.prompt_config["task"],
            {"mime_type": "image/png", "data": image_bytes}
        ]

        try:
            response = model.generate_content(full_prompt)
            # FIX: Explicitly cast to string to satisfy MyPy
            return str(response.text)
        except Exception as e:
            logger.error(f"AI Analysis Failed: {e}")
            return "AI Analysis unavailable due to API limits or error."
