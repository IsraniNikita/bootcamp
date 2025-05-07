def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if not isinstance(args[0], str):  # Assuming first argument should be a string
            print("Invalid argument!")
            return
        return func(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, name):
        self.name = name

    @validate_args
    def update_name(self, name):
        self.name = name
        print(f"Name updated to: {self.name}")


user = User("Alice")
user.update_name("Bob")  # Valid
user.update_name(123)  # Invalid
