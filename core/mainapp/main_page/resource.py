from django.http import JsonResponse
from django.views.generic import View

from .dao import MainPageDao
from .utils import MainPageUtils

from ..models import ServiceStation


class MainPage(View):
    @staticmethod
    def get(request):
        sto: ServiceStation = MainPageDao.get_top_sto_service()

        if sto is None:
            return JsonResponse(
                data={"data": "Data of STO is not exists"},
                status=204
            )

        list_of_sto: list = MainPageUtils.get_data_of_main_page(sto)
        MainPageDao.get_list_and_sort_dict(list_of_sto)

        return JsonResponse(
            data={"data_top_sto": str(list_of_sto[0])},
            safe=False,
            status=200
        )
