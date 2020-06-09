from django.urls import include, path
from rest_framework import routers

from api.modules.series import views as series
from api.modules.location import views as location
from api.modules.series_location import views as series_location


router = routers.DefaultRouter()
router.register(r'series', series.SeriesViewSet, 'SeriesViewSet')
router.register(r'location', location.LocationViewSet, 'LocationViewSet')

urlpatterns = [
    path('', include(router.urls)),

    path('series/<int:series_id>', series.series_detail),
    path('image/cover/<uuid:uuid>', series.cover_image),
    path('popular/series', series.popular_series),

    path('country/', location.countries),
    path('prefecture/<int:country_id>', location.prefectures),
    path('city/<int:prefecture_id>', location.cities),
    path('location/<int:location_id>', location.location_detail),
    path('image/location/<uuid:uuid>', location.location_image),
    path('popular/location', location.popular_locations),

    path('image/series/<uuid:uuid>', series_location.series_location_image),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]