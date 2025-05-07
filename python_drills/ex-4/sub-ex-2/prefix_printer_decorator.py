def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} started")
            result = func(*args, **kwargs)
            print(f"{prefix} {func.__name__} ended")
            return result
        return wrapper
    return decorator

@prefix_printer("Log:")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
