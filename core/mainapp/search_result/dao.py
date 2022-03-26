from typing import Optional

from django.db.models import Avg

from ..models import Review, adding_endings_for_improved_search, MyQuerySet, \
    ServiceStation


class SearchResultDao:
    @staticmethod
    def get_all_service() -> Optional[ServiceStation]:
        return ServiceStation.objects.all()

    @staticmethod
    def get_all_review() -> Optional[Review]:
        return Review.objects.all()

    @staticmethod
    def search_by_word(search_word: str) -> str or None:
        return adding_endings_for_improved_search(search_word)

    @staticmethod
    def get_search_word_and_search(search_word: str) -> \
            Optional[ServiceStation]:
        return ServiceStation.objects.filter(
            servicesto__name__icontains=search_word
        ).distinct()

    @staticmethod
    def get_review_star(service: Optional[ServiceStation]) -> float or None:
        rating = service.reviews.aggregate(Avg('stars'))['stars__avg']

        if rating is None:
            rating = 0
        return rating

    @staticmethod
    def get_name_and_service_check_by_search_word(
            service: Optional[ServiceStation], search_word: str
    ) -> Optional[MyQuerySet]:
        return service.servicesto_set.filter(
                name__icontains=search_word
            ).values('name', 'service_check')
