from uuid import UUID
from typing import Optional
from pydantic import BaseModel, validator

from ..models import ServiceStation


class STOMapValidator(BaseModel):
    sto_uuid: UUID

    @validator('sto_uuid')
    def validator_search_sto(cls, sto_uuid: UUID) -> UUID:
        sto_obj = ServiceStation.objects.get_or_none(sto_uuid=sto_uuid)
        if sto_obj is None:
            raise ValueError('STO id is not exists')
        return sto_uuid
