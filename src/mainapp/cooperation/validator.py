from pydantic import BaseModel, validator

from validate_email import validate_email


class EmailValidator(BaseModel):
    email: str
    message: str

    @validator('email')
    def validator_email(cls, email: str) -> str:
        if not validate_email(email=email):
            raise ValueError('Email is not exists')
        return email

    @validator('message')
    def validator_message(cls, message: str) -> str:
        if message is None:
            raise ValueError('Message is not exists')
        return message
