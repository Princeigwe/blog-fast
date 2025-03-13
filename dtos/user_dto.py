from pydantic import BaseModel, Field

class UserDto(BaseModel):
  email: str = Field(..., max_length=50)
  username: str = Field(..., max_length=50)