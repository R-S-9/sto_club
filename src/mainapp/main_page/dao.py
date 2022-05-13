from typing import Optional
from operator import itemgetter

from django.db.models import Avg

from ..models import ServiceStation


class MainPageDao:
    """Data access object"""
    @staticmethod
    def get_top_sto_service() -> Optional[ServiceStation]:
        return ServiceStation.objects.annotate(
            avg_stars=Avg('reviews__stars')
        ).order_by('-avg_stars').distinct()[:10]

    @staticmethod
    def get_list_and_sort_dict(sto_list: list):
        try:
            return sto_list.sort(key=itemgetter('rating'), reverse=True)
        except Exception:
            return sto_list
