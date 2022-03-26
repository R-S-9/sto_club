from typing import Optional

from ..models import ServiceStation, Review


class ReviewDao:
    """Data access object"""
    @staticmethod
    def get_sto_obj_by_id(sto_id) -> Optional[ServiceStation]:
        return ServiceStation.objects.get_or_none(sto_uuid=sto_id)

    @staticmethod
    def change_review(review_id) -> Optional[Review]:
        return Review.objects.get_or_none(id=review_id)

    @staticmethod
    def get_review_obj_by_id(review_id) -> Optional[Review]:
        return Review.objects.filter(id=review_id).values(
                'review', 'user_name', 'stars', 'date', 'id'
            )
