from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    user = "user"
    staff = "staff"

# Base User Schema
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: RoleEnum

# User Create Schema
class UserCreate(UserBase):
    password: str  # Not stored in DB

# User Response Schema
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# User Update Schema
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    role: Optional[RoleEnum]
