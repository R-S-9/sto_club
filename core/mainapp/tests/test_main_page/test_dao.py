from django.test import TestCase

from ...models import ServiceStation, Review
from ...main_page.dao import MainPageDao


class MainPageDaoTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )
        self.review = Review.objects.create(
            review='Пример теста отзыва',
            id_service_station=self.service_station,
            user_name='Имя пользователя',
            stars=5,
        )

        assert self.service_station
        assert self.review

    def test_get_top_sto_service(self):
        assert MainPageDao.get_top_sto_service()[0].sto_name == \
               self.service_station.sto_name

    def test_get_list_and_sort_dict(self):
        sto_list = [
            {
                'sto_name': self.service_station.sto_name,
                'rating': float('{:.1f}'.format(self.review.stars))
            },
            {
                'sto_name': 'Пример для сравнения',
                'rating': float('{:.1f}'.format(2))
            }
        ]
        MainPageDao.get_list_and_sort_dict(sto_list)

        assert sto_list[0].get('sto_name') == self.service_station.sto_name
