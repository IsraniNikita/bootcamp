import time

@profile
def slow_function():
    time.sleep(2)
    return "Completed"

if __name__ == "__main__":
    slow_function()
