from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User("Nikita", 20)
print(user)
