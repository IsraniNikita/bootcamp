from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

u = User("Frank", 17)
print(u.is_adult())  # False
