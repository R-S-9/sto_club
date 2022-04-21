from django.test import TestCase, RequestFactory

from ...models import ServiceStation
from ...sto_map.resource import STOMap


class STOMapResourceTest(TestCase):
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

        response = STOMap.as_view()(request, self.service_station.sto_uuid)

        assert response.status_code == 200
