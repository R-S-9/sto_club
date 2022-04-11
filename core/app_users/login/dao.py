from typing import Optional

from django.contrib.auth.models import User


class LoginDao:
    @staticmethod
    def get_user_by_email(email) -> Optional[User]:
        return User.objects.get_or_none(email=email)
