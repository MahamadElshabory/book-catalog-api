from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime


class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    username: str = Field(max_length=20)
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)


class UserPublicModel(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_verified: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SignupResponseModel(BaseModel):
    message: str
    user: UserPublicModel
    email_task_id: str


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)


class EmailModel(BaseModel):
    addresses: list[EmailStr]