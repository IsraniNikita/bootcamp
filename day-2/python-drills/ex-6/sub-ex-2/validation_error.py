from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

data = {"name": "Nikita", "age": "not a number"}

try:
    user = User(**data)
except ValidationError as e:
    print(e)
