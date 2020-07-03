from django.urls import include, path

from web.views.index import views as index
from web.views.series import views as series
from web.views.location import views as location

urlpatterns = [
    path('', index.index, name='index'),
    path('series/<int:series_id>', series.detail, name='series'),
    path('series', series.lists, name='series-list'),
    path('location/<int:location_id>', location.detail, name='location'),
    path('location', location.lists, name='location-list')
]
