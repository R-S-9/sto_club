from uuid import UUID

from ..models import Review


class ReviewUtils:
    @staticmethod
    def create_and_post_review(
            user_name: str,
            review: str,
            stars: int,
            sto_uuid: UUID
    ) -> None:
        Review.objects.create(
            review=review,
            id_service_station=sto_uuid,
            user_name=user_name,
            stars=stars
        )

        return None

    @staticmethod
    def change_review(review_data, validation_json) -> None:
        change_review_data = Review.objects.get(id=review_data[0].get('id'))
        change_review_data.review = validation_json.review
        change_review_data.user_name = validation_json.user_name
        change_review_data.stars = validation_json.stars

        change_review_data.save()

        return None

    @staticmethod
    def delete_review(review_id) -> None:
        review = Review.objects.get(id=review_id)
        review.delete()

        return None
