from pydantic import BaseModel

class UserResponse(BaseModel):
  id: int
  email: str
  username: str
  location: str
  # password was not included in order to hide it

  # this helped solve the pydantic.error_wrappers.ValidationError
  class Config:
    orm_mode = True