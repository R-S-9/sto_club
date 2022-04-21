from loguru import logger
from pydantic import ValidationError

from django.views import View
from django.http import JsonResponse

from .dao import RegistrationDao, UserDao
from .validator import RegistrationValidator
from ..mailer.utils import Mailer


logger.add(
    "logs/users_logs.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10MB",
    compression="zip"
)


class Registration(View):
    """Класс регистрации"""
    @staticmethod
    def post(request):
        try:
            validation_json = RegistrationValidator.parse_raw(request.body)
        except ValidationError as _ex:
            logger.info(
                "'AppUser CreateUser Registration post' info:'User "
                f"registration error: {_ex}'"
            )
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=400
            )

        try:
            data = RegistrationDao.create_user(validation_json)
        except Exception:
            data = UserDao.get_user_id_by_email(validation_json.email)

        Mailer.send_mail(validation_json.email, data.id)
        logger.info(
            "'AppUser CreateUser Registration post' info:'User registration "
            f"success: {data.id}'"
        )

        return JsonResponse(
                data={"success": True, "user_id": data.id}, status=201
            )
