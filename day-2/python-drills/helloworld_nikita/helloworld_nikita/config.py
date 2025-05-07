# helloworld_nikita/config.py
import os
import yaml
import logging

logging.basicConfig(level=os.environ.get("PYTHONLOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

def load_config():
    config_path = os.environ.get("CONFIG_PATH")
    if config_path:
        config_file = os.path.join(config_path, "config.yaml")
        try:
            with open(config_file, "r") as f:
                config = yaml.safe_load(f)
                logger.info(f"Loaded config from {config_file}")
                return config
        except FileNotFoundError:
            logger.warning(f"No config file found at {config_file}, using defaults.")
    else:
        logger.info("CONFIG_PATH not set, using default config.")
    return {"message": "Hello"}
