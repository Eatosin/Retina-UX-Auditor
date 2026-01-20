import yaml
import os
import logging
from typing import Dict, Any, cast

logger = logging.getLogger(__name__)

def load_prompt_config(key: str) -> Dict[str, Any]:
    """
    Loads a specific prompt configuration from config/prompts.yaml.
    Returns a dictionary containing role, instructions, etc.
    """
    # Resolve path relative to this file
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    config_path = os.path.join(base_path, "config", "prompts.yaml")

    try:
        with open(config_path, "r") as f:
            data = yaml.safe_load(f)
            
        if key not in data:
            raise KeyError(f"Prompt key '{key}' not found in {config_path}")
            
        # FIX: Explicitly tell MyPy this is a Dictionary
        return cast(Dict[str, Any], data[key])
        
    except Exception as e:
        logger.error(f"Failed to load prompt config: {e}")
        # Fallback to prevent crash
        return {
            "role": "UI Auditor",
            "context_instruction": "Analyze this UI.",
            "task": "Provide feedback."
        }