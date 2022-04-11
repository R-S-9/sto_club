from pydantic import ValidationError

from django.views import View
from django.http import JsonResponse
from django.contrib.auth import login

from .dao import LoginDao
from .validator import LoginValidator
from ..hash_password.utils import HashPassword


class Login(View):
    @staticmethod
    def post(request):
        try:
            validation_json = LoginValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=400
            )

        user = LoginDao.get_user_by_email(validation_json.email)

        if not all([
            user, HashPassword.check_password(
                validation_json.password, user.password
            )
        ]):
            return JsonResponse(
                data={"error": 'password is incorrect'}, status=400
            )

        login(request, user)

        return JsonResponse(data={"success": True}, status=200)
