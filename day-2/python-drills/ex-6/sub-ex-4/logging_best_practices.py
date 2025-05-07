import logging

# Setup Logger with formatting and file output
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Use __name__ as the logger name
logger = logging.getLogger(__name__)

# Flag to control debug-level logging
debug = True

# Sample user object
class User:
    def __init__(self, name):
        self.name = name

# Log at various levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")

# Contextual message
user = User("Nikita")
if debug:
    logger.debug(f"User: {user.name}")

# Replacing print with logger
logger.info("Application started")

# Conditional debug
if debug:
    logger.debug("Debugging mode is ON")
