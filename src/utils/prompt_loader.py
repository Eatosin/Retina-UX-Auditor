import yaml
import os
import logging

logger = logging.getLogger(__name__)

def load_prompt_config(key: str) -> dict:
    """
    Loads a specific prompt configuration from config/prompts.yaml.
    Returns a dictionary containing role, instructions, etc.
    """
    # Resolve path relative to this file
    # Structure: src/utils/ -> ../../config/prompts.yaml
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    config_path = os.path.join(base_path, "config", "prompts.yaml")

    try:
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
            
        if key not in data:
            raise KeyError(f"Prompt key '{key}' not found in {config_path}")
            
        return data[key]
        
    except Exception as e:
        logger.error(f"Failed to load prompt config: {e}")
        # Fallback to prevent crash
        return {
            "role": "UI Auditor",
            "context_instruction": "Analyze this UI.",
            "task": "Provide feedback."
        }
