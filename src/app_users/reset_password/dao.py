from typing import Optional

from django.utils.http import urlsafe_base64_decode

from django.contrib.auth.models import User


class ResetPasswordConfirmDao:
    @staticmethod
    def get_user_by_id(ids) -> Optional[User]:
        return User.objects.get(id=urlsafe_base64_decode(ids).decode())
