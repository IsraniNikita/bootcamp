from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

user = User("Nikita", 25)
print(user)
