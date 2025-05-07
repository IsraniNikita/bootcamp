class DBConnection:
    def __enter__(self):
        print("DB Connected")
        return self

    def __exit__(self, exc_type, exc_val, tb):
        print("DB Disconnected")

with DBConnection():
    print("Running DB operation")
