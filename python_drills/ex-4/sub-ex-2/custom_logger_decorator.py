def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - {func.__name__} started")
            result = func(*args, **kwargs)
            print(f"{message} - {func.__name__} ended")
            return result
        return wrapper
    return decorator

@custom_logger("INFO")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
