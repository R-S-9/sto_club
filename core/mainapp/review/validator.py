from uuid import UUID
from typing import Optional
from pydantic import BaseModel, validator

from ..models import ServiceStation, Review


class ReviewValidator(BaseModel):
    user_name: str
    review: str
    stars: int
    sto_uuid: UUID

    @validator('sto_uuid')
    def validator_search_sto(cls, sto_uuid: UUID) -> Optional[ServiceStation]:
        sto_obj = ServiceStation.objects.get_or_none(sto_uuid=sto_uuid)
        if sto_obj is None:
            raise ValueError('STO id is not exists')
        return sto_obj

    @validator('user_name')
    def validator_user_name(cls, user_name: str) -> str:
        if user_name is None:
            raise ValueError('user name is empty')
        return user_name

    @validator('review')
    def validator_review(cls, review: str) -> str:
        if review is None:
            raise ValueError('user name is empty')
        return review

    @validator('stars')
    def validator_stars(cls, stars: int) -> int:
        if stars > 5 or stars < 1:
            raise ValueError("stars can't be less than zero or greater than 5")
        elif stars is None:
            raise ValueError('stars is empty')
        return stars


class ReviewChangeValidator(BaseModel):
    user_name: str
    review: str
    stars: int
    review_id: int

    @validator('review_id')
    def validator_review_sto(cls, review_id: int) -> int:
        if Review.objects.get_or_none(id=review_id) is None:
            raise ValueError('STO id is not exists')
        return review_id

    @validator('user_name')
    def validator_user_name(cls, user_name: str) -> str:
        if user_name is None:
            raise ValueError('user name is empty')
        return user_name

    @validator('review')
    def validator_review(cls, review: str) -> str:
        if review is None:
            raise ValueError('user name is empty')
        return review

    @validator('stars')
    def validator_stars(cls, stars: int) -> int:
        if stars > 5 or stars < 1:
            raise ValueError("stars can't be less than zero or greater than 5")
        elif stars is None:
            raise ValueError('stars is empty')
        return stars


class ReviewDeleteValidator(BaseModel):
    review_id: int

    @validator('review_id')
    def validator_review_sto(cls, review_id: int) -> int:
        if Review.objects.get_or_none(id=review_id) is None:
            raise ValueError('STO id is not exists')
        return review_id
