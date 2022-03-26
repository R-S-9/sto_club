from ..models import ServiceStation
from ..search_result.dao import SearchResultDao


class MainPageUtils:
    """list of top STO"""
    @staticmethod
    def get_data_of_main_page(sto: ServiceStation) -> list:
        list_of_sto = []

        for station in sto:
            rating = SearchResultDao.get_review_star(station)

            list_of_sto.append({
                'sto_name': station.sto_name,
                'sto_id': station.sto_uuid,
                'description_sto': station.description_sto,
                'rating': float('{:.1f}'.format(rating)),
                'image': station.images.values('image_sto')
            })

        return list_of_sto
