from django.http import JsonResponse
from django.views import View
from pydantic import ValidationError

from .validator import EmailValidator

from ..mailer.utils import Mailer


class Cooperation(View):
    @staticmethod
    def post(request):
        try:
            validation_json = EmailValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        if not Mailer.send_mail(
                validation_json.email, validation_json.message
        ):
            return JsonResponse(
                data={"error": "sending message"}, status=400
            )
        return JsonResponse(
            data={"data": "message sent successfully "}, status=200
        )
