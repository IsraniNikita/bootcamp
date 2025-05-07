from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Dave", 40)
print("Before mutation:", u)

try:
    u.age = 41  # This line will raise FrozenInstanceError
except FrozenInstanceError as e:
    print("Caught immutability error:", e)
