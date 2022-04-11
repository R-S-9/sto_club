from django.views import View
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode

from .dao import UserPersonalDataDao


class UserPersonalData(View):
    @staticmethod
    def get(request, uid):
        if isinstance(uid, str):
            uid = urlsafe_base64_decode(uid).decode()

        data = UserPersonalDataDao.get_user_by_id(uid)

        if not data:
            return JsonResponse(
                {'data': {'error': "not found user"}}, status=400
            )

        return JsonResponse({'data': data}, status=200)
