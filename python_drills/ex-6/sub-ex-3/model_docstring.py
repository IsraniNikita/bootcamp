from pydantic import BaseModel, Field

class User(BaseModel):
    """
    User model for application identity and authentication.
    """
    name: str
    email: str = Field(..., description="Email used for contact and login.")

user = User(name="Nikita", email="nikitaisrani08@gmail.com")
print(user)
