from django.test import TestCase

from ...models import ServiceStation, Review
from ...main_page.utils import MainPageUtils


class MainPageUtilsTest(TestCase):
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

    def test_get_data_of_main_page(self):
        sto_list = MainPageUtils.get_data_of_main_page(
            ServiceStation.objects.filter(
                sto_uuid=self.service_station.sto_uuid
            )
        )

        assert sto_list[0].get('sto_id') == self.service_station.sto_uuid
