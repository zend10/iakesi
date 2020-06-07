from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('country/', views.countries),
    path('prefecture/<int:country_id>', views.prefectures),
    path('city/<int:prefecture_id>', views.cities),
    path('series/', views.series),
    path('series/<int:series_id>', views.series_detail),
    path('location/', views.locations),
    path('location/<int:location_id>', views.location_detail),
    path('image/cover/<uuid:uuid>', views.cover_image),
    path('image/location/<uuid:uuid>', views.location_image),
    path('image/series/<uuid:uuid>', views.series_location_image),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]