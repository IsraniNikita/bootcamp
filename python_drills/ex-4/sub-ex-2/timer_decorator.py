import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def greet(name):
    time.sleep(1)  # Simulating a delay
    print(f"Hello, {name}!")

greet("Alice")
