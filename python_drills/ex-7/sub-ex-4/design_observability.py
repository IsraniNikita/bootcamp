import logging
import time
import os
import random
import psutil
from functools import wraps


DEBUG = True


logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)



def log_with_context(user_id, function_name, message, error_id=None):
    full_message = f"[User: {user_id}] [{function_name}] {message}"
    if error_id:
        full_message += f" [Error ID: {error_id}]"
    logger.info(full_message)



def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logger.info(f"[{func.__name__}] executed in {duration:.4f}s")
        return result

    return wrapper



def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} returned {result}")
        return result

    return wrapper



metrics = {
    "calls": 0,
    "errors": 0,
    "total_time": 0
}


@timed
@trace
def compute_score(user_id):
    metrics["calls"] += 1
    score = random.randint(0, 100)
    time.sleep(random.uniform(0.1, 0.3))
    if score < 10:
        metrics["errors"] += 1
        log_with_context(user_id, "compute_score", "Score too low", error_id="E1001")
    return score



def health_check():
    return {"status": "OK", "uptime": f"{time.time() - START:.2f}s"}



def print_resources():
    logger.info(f"Memory usage: {psutil.virtual_memory().percent}%")
    logger.info(f"CPU usage: {psutil.cpu_percent()}%")



START = time.time()

if __name__ == "__main__":
    user_id = "user_42"
    for _ in range(3):
        score = compute_score(user_id)
        log_with_context(user_id, "main", f"Score computed: {score}")

    logger.info(f"Health Check: {health_check()}")
    logger.info(f"Metrics: {metrics}")
    print_resources()
