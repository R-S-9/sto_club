from django.test import TestCase

from ...models import ServiceStation
from ...sto_map.utils import STOMapUtils


class STOMapUtilsTest(TestCase):
    def setUp(self) -> None:
        self.service_station = ServiceStation.objects.create(
            sto_name="СТО тест",
            location="СТО тест локация",
            location_coordinates="СТО тест координаты локации",
            description_sto="СТО тест описание",
            about_sto="СТО тест полное описание",
        )

        assert self.service_station

    def test_get_data_of_services(self):
        sto_list = STOMapUtils.get_data_of_service_by_obj(
            self.service_station.sto_uuid
        )

        assert sto_list[0].get("sto_id") == self.service_station.sto_uuid
