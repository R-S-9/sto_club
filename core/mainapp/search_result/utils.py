from typing import Optional

import django_filters

from .dao import SearchResultDao
from ..models import MyQuerySet, ServiceStation


class SearchResultUtils:
    @staticmethod
    def get_data_of_services(
            services: Optional[MyQuerySet], search_word: str
    ) -> list:
        data = []

        for all_service in services:
            rating = SearchResultDao.get_review_star(all_service)

            desired_service: Optional[MyQuerySet] = SearchResultDao. \
                get_name_and_service_check_by_search_word(
                    all_service, search_word
                )

            data.append({
                'sto_name': all_service.sto_name,
                'sto_id': all_service.sto_uuid,
                'service': [
                    {
                        'name': srv['name'], 'check': srv['service_check']
                    } for srv in desired_service
                ],
                'description_sto': all_service.description_sto,
                'about_sto': all_service.about_sto,
                'location': all_service.location,
                'rating': float('{:.1f}'.format(rating)),
                'image': all_service.images.values('image_sto')
            })

            return data


class STOFilter(django_filters.FilterSet):

    class Meta:
        model = ServiceStation
        fields = '__all__'
