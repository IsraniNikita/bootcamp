from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function is being called!")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name"""
    return f"Hello, {name}!"

print(greet.__name__)  # Should print 'greet'
print(greet.__doc__)   # Should print 'Greets a person by name'
print(greet("Alice"))  # Function is being called! Output: Hello, Alice!
