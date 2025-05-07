from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Eve", 22)
u2 = User("Eve", 22)
print(u1 == u2)  # True
