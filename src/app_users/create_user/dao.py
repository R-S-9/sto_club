import json
from typing import Optional

from django.contrib.auth.models import User

from ..hash_password.utils import HashPassword


class RegistrationDao:
    @staticmethod
    def create_user(user_json: json) -> Optional[User]:
        return User.objects.get_or_create(
            full_name=user_json.full_name,
            email=user_json.email,
            password=HashPassword.get_hashed_password(
                user_json.password
            )
        )[0]


class UserDao:
    @staticmethod
    def get_user_id_by_email(email) -> Optional[User]:
        return User.objects.get_or_none(email=email)
