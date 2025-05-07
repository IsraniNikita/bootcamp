from pydantic import BaseModel, validator

class User(BaseModel):
    name: str

    @validator("name")
    def must_be_capitalized(cls, value):
        if not value[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return value


try:
    user_lower = User(name="miki")
    print(f"name='{user_lower.name}'")
except Exception as e:
    print(f"Error creating user with lowercase name: {e}")

# This should pass the validation
user_upper = User(name="Nikita")
print(f"name='{user_upper.name}'")

