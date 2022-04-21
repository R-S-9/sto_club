from django.test import TestCase

from ...models import ServiceStation, Review, ServiceSTO
from ...search_result.dao import SearchResultDao


class SearchResultDaoTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )
        self.service_sto = ServiceSTO.objects.create(
            name='Пример услуги',
            service_check=599,
            service=self.service_station
        )
        self.review = Review.objects.create(
            review='Пример теста отзыва',
            id_service_station=self.service_station,
            user_name='Имя пользователя',
            stars=5,
        )

        assert self.service_station
        assert self.service_sto
        assert self.review

    def test_get_all_service(self):
        sto = SearchResultDao.get_all_service().first()

        assert sto.sto_uuid == self.service_station.sto_uuid

    def test_get_all_review(self):
        review = SearchResultDao.get_all_review().first()

        assert review.id == self.review.id

    def test_search_by_word(self):
        search = SearchResultDao.search_by_word(
            search_word=self.service_sto.name
        )
        assert search == 'Пример'

    def test_get_search_word_and_search(self):
        search_word = SearchResultDao.get_search_word_and_search(
            'Услуги'
        ).first()

        assert search_word.sto_name == self.service_station.sto_name

    def test_get_review_star(self):
        sto_star = SearchResultDao.get_review_star(self.service_station)

        assert sto_star == self.review.stars

    def test_get_name_and_service_check_by_search_word(self):
        sto_obj = SearchResultDao.get_name_and_service_check_by_search_word(
            self.service_station, 'Пример услуги'
        )

        assert sto_obj[0].get("name") == self.service_sto.name
