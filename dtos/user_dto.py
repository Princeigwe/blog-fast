from pydantic import BaseModel, Field
from enums.roles_enums import Role

class UserDto(BaseModel):
  email: str = Field(..., max_length=50)
  username: str = Field(..., max_length=50)
  password: str = Field(..., max_length=50)
  role: Role = Field(default=Role.customer)