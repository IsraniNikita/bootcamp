from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

@dataclass
class AdminUser(User):
    access_level: int = 1

admin = AdminUser("Grace", 35, 5)
print(admin)
