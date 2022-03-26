import json

from django.test import TestCase, RequestFactory

from ...models import ServiceStation, ServiceSTO
from ...search_result.resource import SearchResult


class SearchResultResourceTest(TestCase):
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
        self.factory = RequestFactory()

        assert self.service_station
        assert self.service_sto
        assert self.factory

    def test_post(self):
        request = self.factory.post('')
        request._body = json.dumps({"search": 'Пример услуги'})
        request.content_type = 'application/json'

        response = SearchResult.as_view()(request)

        assert response.status_code == 200
