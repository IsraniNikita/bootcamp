from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(..., description="User's email address")

user = User(email="nikitaisrani08@gmail.com")
print(user)
