import logging
import os
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Retina")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    logger.info(f"Retina System Starting on Port {port}...")
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=False)
