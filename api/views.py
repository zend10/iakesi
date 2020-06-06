from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    SeriesSerializer, SeriesImageSerializer, LocationSerializer, SeriesLocationSerializer, LocationSeriesSerializer
)
from .models import Series, Location, SeriesLocation
from Real2D.settings import BASE_DIR

import os


def _get_locations_from_series(series_id):
    location_list = SeriesLocation.objects.filter(series=series_id).select_related()
    location_serializer = SeriesLocationSerializer(location_list, many=True)
    return location_serializer.data


def _get_series_from_location(location_id):
    series_list = SeriesLocation.objects.filter(location=location_id).select_related()
    series_serializer = LocationSeriesSerializer(series_list, many=True)
    return series_serializer.data


@api_view(['GET'])
def series(request):
    series_list = Series.objects.all().order_by('name')
    series_serializer = SeriesSerializer(series_list, many=True)
    return Response(series_serializer.data)


@api_view(['GET'])
def series_detail(request, series_id):
    try:
        series_item = Series.objects.get(id=series_id)
    except Series.DoesNotExist:
        return Response(status=404)

    series_serializer = SeriesSerializer(series_item)
    response = series_serializer.data
    response['locations'] = _get_locations_from_series(series_id)
    return Response(response)


@api_view(['GET'])
def locations(request):
    location_list = Location.objects.all()
    location_serializer = LocationSerializer(location_list, many=True)
    return Response(location_serializer.data)


@api_view(['GET'])
def location_detail(request, location_id):
    try:
        location_item = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return Response(status=404)

    location_serializer = LocationSerializer(location_item)
    response = location_serializer.data
    response['series'] = _get_series_from_location(location_id)
    return Response(response)


@api_view(['GET'])
def cover_image(request, uuid):
    try:
        series_item = Series.objects.get(image_name=uuid)
    except Series.DoesNotExist:
        return HttpResponse(status=404)

    series_serializer = SeriesImageSerializer(series_item)
    image = series_serializer.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return HttpResponse(status=404)


