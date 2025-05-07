from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("George", 25)
u2 = User("George", 25)
print(u1 == u2)  # True
