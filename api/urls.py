from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('series/', views.series),
    path('series/<int:series_id>', views.series_detail),
    path('location/', views.locations),
    path('location/<int:location_id>', views.location_detail),
    path('cover/<uuid:uuid>', views.cover_image),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]