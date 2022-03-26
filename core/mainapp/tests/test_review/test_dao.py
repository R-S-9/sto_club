from django.test import TestCase

from ...models import ServiceStation, Review
from ...review.dao import ReviewDao


class ReviewDaoTest(TestCase):
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

    def test_get_sto_obj_by_id(self):
        sto_obj = ReviewDao.get_sto_obj_by_id(self.service_station.sto_uuid)

        assert sto_obj.sto_name == self.service_station.sto_name

    def test_change_review(self):
        review_obj = ReviewDao.change_review(self.review.id)

        assert review_obj.review == self.review.review

    def test_get_review_obj_by_id(self):
        review_obj = ReviewDao.get_review_obj_by_id(self.review.id)

        assert review_obj[0].get("review") == self.review.review
