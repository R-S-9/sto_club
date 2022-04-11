from pydantic import BaseModel, validator


class LogoutValidator(BaseModel):
    email: str

    @validator('email')
    def validator_email(cls, email: str) -> None:
        if email is None:
            raise ValueError('Email is not exist')
