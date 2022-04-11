from django.contrib.auth.models import User


class ActivateUserUtils:
    @staticmethod
    def activate_user(user: User) -> None:
        user.is_active = True
        user.save()

        return None
