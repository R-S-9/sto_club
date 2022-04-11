from pydantic import BaseModel, validator

from ..models import UserProfile


class LoginValidator(BaseModel):
    email: str
    password: str

    @validator('email')
    def validator_email(cls, email: str) -> str:
        if email is None:
            raise ValueError('Email is not exist')

        user = UserProfile.objects.get_or_none(email=email)

        if user is None or user.is_active is False:
            raise ValueError('Return to registration')
        return email

    @validator('password')
    def validator_password(cls, password: str) -> str:
        if password is None:
            raise ValueError('Password is not exist')
        elif len(password) < 5:
            raise ValueError('Easy password')
        return password
