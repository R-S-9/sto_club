from typing import Optional

from django.contrib.auth.models import User


class ActivateUserDao:
    @staticmethod
    def get_user_by_id(user_id: str) -> Optional[User]:
        return User.objects.get_or_none(id=user_id)
