from pydantic import ValidationError

from django.http import JsonResponse
from django.views.generic import View

from .dao import SearchResultDao
from .utils import SearchResultUtils
from .validator import SearchWordValidator

from ..main_page.dao import MainPageDao
from ..suggest_search_word.utils import SuggestWord


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
            corrected_words = SuggestWord.get_search_word_by_guess(search_word)
            if not corrected_words:
                return JsonResponse(
                    data={"error": "Введенные вами услуги, не найдены"},
                    status=200
                )
            # Должны найти все MyQuerySet и передать их в services
            services, search_word = SearchResultUtils.\
                get_data_for_list_of_search_options(corrected_words)

        if not services:
            return JsonResponse(
                data={"error": "Введенные вами услуги, не найдены"},
                status=400
            )

        data: list = SearchResultUtils.get_data_of_services(
            services, search_word
        )
        MainPageDao.get_list_and_sort_dict(data)

        return JsonResponse(
            data={"data_service": data},
            status=200
        )
