from pydantic import BaseModel, EmailStr, constr
from enum import Enum
from typing import Optional


# Enum for roles
class UserRole(str, Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    first_name: constr(max_length=100) = None
    last_name: constr(max_length=100) = None
    role: UserRole


class UserCreate(UserBase):
    password: constr(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    first_name: constr(max_length=100) = None
    last_name: constr(max_length=100) = None
    password: constr(min_length=8, max_length=128) = None
    email: EmailStr = None
    role: UserRole = None


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# Schema for User Login (Returned by /auth/me)
class UserLogin(UserBase):
    id: int


# Authentication tokens
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
