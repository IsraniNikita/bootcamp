import random

def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying...")
        return wrapper
    return decorator

@retry(max_retries=3)
def unreliable_function():
    if random.random() < 0.5:
        raise ValueError("Random failure")
    return "Success!"

print(unreliable_function())
