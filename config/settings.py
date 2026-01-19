
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Retina UX Auditor"
    VERSION: str = "1.0.0"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    PORT: int = int(os.getenv("PORT", 7860))
    
    # Physics Thresholds
    CLUTTER_THRESHOLD_LOW: int = 10
    CLUTTER_THRESHOLD_HIGH: int = 50

settings = Settings()
