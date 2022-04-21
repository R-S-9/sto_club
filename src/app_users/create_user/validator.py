from typing import Optional

from pydantic import BaseModel, validator

from ..models import UserProfile


class RegistrationValidator(BaseModel):
    full_name: str
    email: str or UserProfile
    password: str

    @validator('full_name')
    def validator_full_name(cls, full_name: str) -> str:
        if full_name is None:
            raise ValueError('Name is not exists')
        return full_name

    @validator('email')
    def validator_email(cls, email: str) -> str or Optional[UserProfile]:
        if email is None:
            raise ValueError('Email is not exists')

        email_exs = UserProfile.objects.get_or_none(email=email)

        if email_exs is None:
            return email
        if email_exs.is_active is True:
            raise ValueError('Email already in use(!)')

    @validator('password')
    def validator_password(cls, password: str) -> str:
        if password is None:
            raise ValueError('Password is not exists')
        return password
