from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SeriesSerializer
from .handlers import *


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = get_all_series()
    serializer_class = SeriesSerializer
    http_method_names = ['get']


@api_view(['GET'])
def series_detail(request, series_id):
    return Response(**get_series_detail(series_id))


@api_view(['GET'])
def cover_image(request, uuid):
    return HttpResponse(**get_cover_image(uuid))


@api_view(['GET'])
def popular_series(request):
    return Response(**get_popular_series())
