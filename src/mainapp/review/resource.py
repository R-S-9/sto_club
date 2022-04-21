from pydantic import ValidationError

from django.http import JsonResponse
from django.views.generic import View

from .dao import ReviewDao
from .utils import ReviewUtils
from .validator import ReviewValidator, ReviewChangeValidator,\
    ReviewDeleteValidator


class ReviewResource(View):
    @staticmethod
    def post(request):
        try:
            validation_json = ReviewValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        ReviewUtils.create_and_post_review(
            user_name=validation_json.user_name,
            review=validation_json.review,
            stars=validation_json.stars,
            sto_uuid=validation_json.sto_uuid
        )

        return JsonResponse(
            data={
                'data': {'review': 'successfully created'}
            },
            status=201
        )

    @staticmethod
    def put(request):
        try:
            validation_json = ReviewChangeValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        ReviewUtils.change_review(
            ReviewDao.get_review_obj_by_id(validation_json.review_id),
            validation_json
        )

        return JsonResponse(
            data={
                'data': {'review': 'successfully change'}
            },
            status=201
        )

    @staticmethod
    def delete(request):
        try:
            validation_json = ReviewDeleteValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        ReviewUtils.delete_review(validation_json.review_id)

        return JsonResponse(
            data={
                'data': {'review': 'is deleted'}
            },
            status=200
        )
