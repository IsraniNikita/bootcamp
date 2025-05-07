from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Nikita", 20)
print(u)
