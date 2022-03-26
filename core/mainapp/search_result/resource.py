from pydantic import ValidationError

from django.http import JsonResponse
from django.views.generic import View

from .dao import SearchResultDao
from .utils import SearchResultUtils
from .validator import SearchWordValidator

from ..main_page.dao import MainPageDao


class SearchResult(View):
    @staticmethod
    def post(request):
        try:
            search_word = SearchWordValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error: {_ex}"}, status=403
            )

        search_word = SearchResultDao.search_by_word(
            search_word.search.rstrip()
        )
        services = SearchResultDao.get_search_word_and_search(search_word)

        if not services.exists():
            return JsonResponse(
                data={"error": "Введенные вами услуги, не найдены"},
                status=200
            )

        data: list = SearchResultUtils.get_data_of_services(
            services, search_word
        )
        MainPageDao.get_list_and_sort_dict(data)

        return JsonResponse(data={"data_service": str(data[0])}, status=200)
