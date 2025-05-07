from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age must be non-negative")

user = User("Nikita", 20)
print(user)
