# helloworld_nikita/hello.py
from .config import load_config
import logging

logger = logging.getLogger(__name__)

def say_hello(name: str):
    config = load_config()
    message = config.get("message", "Hello")
    logger.debug(f"Greeting {name} with message: {message}")
    print(f"{message}, {name}!")
