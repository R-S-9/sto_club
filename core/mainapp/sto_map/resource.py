import json

from django.http import JsonResponse
from django.views.generic import View
from pydantic import ValidationError

from .dao import STOMapDao
from .utils import STOMapUtils
from .validator import STOMapValidator


class STOMap(View):
    @staticmethod
    def get(request, sto_uuid=None):
        try:
            sto_obj = STOMapValidator.parse_raw(
                json.dumps({"sto_uuid": str(sto_uuid)})
            )
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error {_ex}"}, status=403
            )

        list_map_sto = STOMapUtils.get_data_of_service_by_obj(sto_obj.sto_uuid)

        return JsonResponse(
            data={"sto_data": str(list_map_sto[0])},
            status=200,
            safe=False
        )
