from django.test import TestCase

from ...models import ServiceStation
from ...sto_map.dao import STOMapDao


class STOMapDaoTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )

        assert self.service_station

    def test_get_sto_by_uuid(self):
        sto = STOMapDao.get_sto_by_uuid(self.service_station.sto_uuid)

        assert str(sto[0]) == str(self.service_station.sto_name)
