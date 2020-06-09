from django.urls import include, path
# from . import views

from web.views.index import views as index

urlpatterns = [
    path('', index.index),
    # path('series/<int:series_id>', views.series)
]
