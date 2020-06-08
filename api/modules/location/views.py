from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import LocationSerializer
from .handlers import *


class LocationViewSet(viewsets.ModelViewSet):
    queryset = get_all_locations()
    serializer_class = LocationSerializer
    http_method_names = ['get']


@api_view(['GET'])
def countries(request):
    return Response(**get_countries())


@api_view(['GET'])
def prefectures(request, country_id):
    return Response(**get_prefectures(country_id))


@api_view(['GET'])
def cities(request, prefecture_id):
    return Response(**get_cities(prefecture_id))


@api_view(['GET'])
def location_detail(request, location_id):
    return Response(**get_location_detail(location_id))


@api_view(['GET'])
def location_image(request, uuid):
    return HttpResponse(**get_location_image(uuid))
