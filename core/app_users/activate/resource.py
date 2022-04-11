import json

from loguru import logger
from pydantic import ValidationError

from django.views import View
from django.http import JsonResponse

from .dao import ActivateUserDao
from .utils import ActivateUserUtils
from .validator import ActivateValidator
from ..redis_key.utils import CreateRedisKey


logger.add(
    "logs/users_logs.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10MB",
    compression="zip"
)


class ActivateUser(View):
    """Класс активации пользователя через почту"""
    @staticmethod
    def get(request, uuid):
        red = CreateRedisKey()

        try:
            validation_json = ActivateValidator.parse_raw(
                json.dumps({"redis_uuid": red.get(uuid).decode('UTF-8')})
            )
        except ValidationError as _ex:
            logger.info(
                "'AppUser Activate ActivateUser get' info:'User activate error"
                f": {_ex}'"
            )
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=400
            )

        user = ActivateUserDao.get_user_by_id(validation_json.redis_uuid)

        if not user:
            return JsonResponse(
                data={"error": "User is not exist"}, status=400
            )

        ActivateUserUtils.activate_user(user)

        logger.info(
            f"'AppUser Activate ActivateUser get' info:'User {user.email} is "
            "activate'"
        )

        return JsonResponse(
                data={"success": True}, status=200
            )
