from django.test import TestCase, RequestFactory

from ...models import ServiceStation
from ...main_page.resource import MainPage


class MainPageResourceTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )
        self.factory = RequestFactory()

        assert self.service_station
        assert self.factory

    def test_get(self):
        request = self.factory.get('')
        request.content_type = 'application/json'

        response = MainPage.as_view()(request)

        assert response.status_code == 200
