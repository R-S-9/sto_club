import json
from pydantic import ValidationError

from django.views import View
from django.http import JsonResponse
from django.contrib.auth import logout

from .validator import LogoutValidator


class Logout(View):
    @staticmethod
    def get(request):
        try:
            LogoutValidator.parse_raw(json.dumps({"email": str(request.user)}))
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        logout(request)

        return JsonResponse(
                data={"success": True}, status=200
            )
