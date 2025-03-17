from sqlalchemy import Column, Integer, String, Enum
from configuration.config import Base
import enum

class RoleEnum(str, enum.Enum):
    user = "user"
    staff = "staff"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
