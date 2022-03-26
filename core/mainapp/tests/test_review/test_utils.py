from django.test import TestCase

from ...models import ServiceStation, Review
from ...review.utils import ReviewUtils
from ...review.validator import ReviewValidator


class ReviewUtilsTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )

        self.validator = ReviewValidator(
            user_name='Имя пользователя',
            review='Отзыв пример',
            stars=5,
            sto_uuid=self.service_station.sto_uuid
        )

        assert self.service_station
        assert self.validator

    def test_get_data_of_main_page(self):
        ReviewUtils.create_and_post_review(
            'NoName', 'Неплохо', 5, self.service_station
        )

        assert Review.objects.get_or_none(
            id_service_station=self.service_station.sto_uuid
        )

    def test_change_review(self):
        ReviewUtils.create_and_post_review(
            'NoName', 'Неплохо', 5, self.service_station
        )

        ReviewUtils.change_review(
            [{"id": Review.objects.get_or_none(
                id_service_station=self.service_station.sto_uuid
            ).id}],
            self.validator
        )

        assert Review.objects.get_or_none(
            id_service_station=self.service_station.sto_uuid
        ).review == self.validator.review

    def test_delete_review(self):
        ReviewUtils.create_and_post_review(
            'NoName', 'Неплохо', 5, self.service_station
        )
        ReviewUtils.delete_review(Review.objects.get_or_none(
            id_service_station=self.service_station.sto_uuid
         ).id)

        assert Review.objects.all().first() is None
