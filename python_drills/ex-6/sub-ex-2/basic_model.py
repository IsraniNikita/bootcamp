from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

data = {"name": "Nikita", "age": 20}
user = User(**data)
print(user)
