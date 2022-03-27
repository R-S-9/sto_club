from django.urls import path

from .main_page.resource import MainPage
from .search_result.resource import SearchResult
from .sto_map.resource import STOMap
from .review.resource import ReviewResource
from .cooperation.resource import Cooperation
from .info_list_live.resource import InfoListView


urlpatterns = [
    # WEB
    path('main/', MainPage.as_view(), name='main_page'),
    path('search/', SearchResult.as_view(), name='search_result'),
    path('service-map/<uuid:sto_uuid>/', STOMap.as_view(), name='service_map'),
    path(
        'service-map/review/', ReviewResource.as_view(), name='create_review'
    ),
    path('cooperation/', Cooperation.as_view(), name='cooperation_map'),
    path('info_list/', InfoListView.as_view(), name='info_list'),
]
