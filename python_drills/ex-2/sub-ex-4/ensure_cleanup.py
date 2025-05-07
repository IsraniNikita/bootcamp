class Cleaner:
    def __enter__(self):
        print("Setup")
        return self

    def __exit__(self, exc_type, exc_val, tb):
        print("Cleanup even if error occurred")

with Cleaner():
    print("Raising an error...")
    raise ValueError("Oops")
