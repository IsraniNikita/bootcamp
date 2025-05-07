from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)

user = User("Nikita", 20)
print(user)
