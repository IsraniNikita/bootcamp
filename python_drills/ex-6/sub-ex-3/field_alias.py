from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")

data = {"user_id": 101}
user = User(**data)
print(user)
print(user.model_dump(by_alias=True))
