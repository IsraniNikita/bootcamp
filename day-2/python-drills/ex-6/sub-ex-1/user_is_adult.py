from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

user = User("Eva", 17)
print("Is adult?", user.is_adult())
