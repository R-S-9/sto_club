from django.test import TestCase

from ...models import ServiceStation, Review, ServiceSTO
from ...search_result.utils import SearchResultUtils


class SearchResultUtilsTest(TestCase):
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

    def test_get_data_of_services(self):
        sto_list = SearchResultUtils.get_data_of_services(
            ServiceStation.objects.filter(
                sto_uuid=self.service_station.sto_uuid
            ), self.review.review
        )

        assert sto_list[0].get("sto_id") == self.service_station.sto_uuid
