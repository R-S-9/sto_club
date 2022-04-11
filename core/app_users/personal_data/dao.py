from typing import Optional

from django.contrib.auth.models import User


class UserPersonalDataDao:
    @staticmethod
    def get_user_by_id(ids) -> Optional[User]:
        return User.objects.filter(
            id=ids,
            is_active=True
        ).values('id', 'first_name', 'last_name', 'email', 'is_active')
