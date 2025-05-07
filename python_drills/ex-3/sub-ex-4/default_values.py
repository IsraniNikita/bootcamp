from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

u1 = User("Nikita")
u2 = User("Naina", 25)
print(u1, u2)
