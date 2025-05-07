from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Nikita", age=20)
print(user.model_dump())
print(user.model_dump_json())