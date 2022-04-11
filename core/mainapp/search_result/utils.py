from typing import Optional

import django_filters

from .dao import SearchResultDao
from ..models import MyQuerySet, ServiceStation


class SearchResultUtils:
    @staticmethod
    def get_data_for_list_of_search_options(list_words) \
            -> list:
        query_set_list = []  # Сюда добавляем все найденные нами услуги из бд
        found_words = []

        for word in list_words:
            found = SearchResultDao.get_search_word_and_search(word)

            if found.exists():
                query_set_list.append(found)
                found_words.append(word)

        query_set_list = list(set(query_set_list))

        return [
            query_set_list[0] if len(query_set_list) > 0 else None, found_words
        ]

    @staticmethod
    def get_data_of_services(
            services: Optional[MyQuerySet], search_word: str
    ) -> list:
        data = []

        for all_service in services:
            rating = SearchResultDao.get_review_star(all_service)

            desired_service: Optional[MyQuerySet] = SearchResultDao. \
                get_name_and_service_check_by_search_word(
                    all_service,
                    search_word[0] if type(search_word) is list else
                    search_word
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
