from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

data = {
    "name": "Nikita",
    "age": 20,
    "profile": {"bio": "Hello!", "website": "https://example.com"}
}

user = User(**data)
print(user)
