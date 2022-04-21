from uuid import UUID

from ..search_result.dao import SearchResultDao
from .dao import STOMapDao

from ..models import ServiceStation


class STOMapUtils:
    @staticmethod
    def get_data_of_service_by_obj(sto_uuid: UUID) -> list:
        data = []
        sto_obj: ServiceStation = STOMapDao.get_sto_by_uuid(sto_uuid)

        for sto in sto_obj:
            rating = SearchResultDao.get_review_star(sto)

            data.append({
                'sto_name': sto.sto_name,
                'sto_id': sto.sto_uuid,
                'service': [
                    sto.servicesto_set.order_by('name').values(
                        'name', 'service_check'
                    )
                ],
                'description_sto': sto.description_sto,
                'about_sto': sto.about_sto,
                'location': sto.location,
                'rating': float('{:.1f}'.format(rating)),
                'image': sto.images.values('image_sto'),
                'reviews': sto.reviews.order_by('-date').values(
                    'review', 'stars', 'user_name', 'date', 'id'
                ),
            })

        return data
