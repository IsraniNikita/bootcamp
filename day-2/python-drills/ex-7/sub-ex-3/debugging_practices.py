import pdb
import traceback
import logging
import warnings

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# 1. Function with pdb.set_trace()
def divide(a, b):
    pdb.set_trace()  # Execution will pause here
    return a / b

# 2. breakpoint() (Python 3.7+)
def add(a, b):
    breakpoint()  # Recommended modern way
    return a + b

# 3. traceback module example
def might_fail():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Traceback info:")
        print(traceback.format_exc())

# 4. Structured logging
def process_data(x):
    logger.debug("Entering process_data with x=%s", x)
    result = x ** 2
    logger.debug("Exiting process_data with result=%s", result)
    return result

# 5. Warnings module
def deprecated_function():
    warnings.warn("This function is deprecated", DeprecationWarning)

# 6. Verbose exception info
def error_demo():
    try:
        int("not_a_number")
    except Exception as e:
        print("Verbose Exception:")
        print(type(e), e)

# 7. Debug recursive call stack
def factorial(n, level=0):
    logger.debug("Level %d: factorial(%d)", level, n)
    if n <= 1:
        return 1
    return n * factorial(n - 1, level + 1)

# 8. Fail loud then graceful
def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Age must be positive")
    except ValueError as e:
        logger.error("Validation failed: %s", e)
        raise

# === RUN ===
if __name__ == "__main__":
    # Comment/uncomment as needed
    # divide(10, 2)
    # print(add(3, 5))
    might_fail()
    print(process_data(4))
    deprecated_function()
    error_demo()
    print("Factorial:", factorial(4))
    try:
        validate_age(-5)
    except Exception as e:
        print("Handled in main:", e)
