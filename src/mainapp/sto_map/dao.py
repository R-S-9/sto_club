from uuid import UUID
from typing import Optional

from ..models import ServiceStation


class STOMapDao:
    @staticmethod
    def get_sto_by_uuid(sto_uuid: UUID) -> Optional[ServiceStation]:
        return ServiceStation.objects.filter(
            sto_uuid=sto_uuid
        )
