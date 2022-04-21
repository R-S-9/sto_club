import json

from django.http import JsonResponse
from django.views import View

from .utils import SetNewPassword
from .dao import ResetPasswordConfirmDao


class ResetPasswordConfirm(View):
    @staticmethod
    def post(request, uid, token=None):
        data = json.loads(request.body)
        user = ResetPasswordConfirmDao.get_user_by_id(uid)

        if all([data['new_password'], user, len(data['new_password']) > 5]):
            SetNewPassword.set_new_password(user, data['new_password'])

            return JsonResponse(
                data={"data": {"password": "success"}}, status=200
            )
        return JsonResponse(
            data={
                "data": {"error": "HTTP_400_BAD_REQUEST or get new_password"}
                },
            status=400
        )
