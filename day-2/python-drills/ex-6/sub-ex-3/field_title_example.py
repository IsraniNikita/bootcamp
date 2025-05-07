from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., title="Username", example="jnikita_israni")

user = User(username="nikita_israni")
print(user)
