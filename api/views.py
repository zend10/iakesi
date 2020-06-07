import os

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    CountrySerializer,
    PrefectureSerializer,
    CitySerializer,
    SeriesSerializer,
    SeriesImageSerializer,
    LocationSerializer,
    LocationImagePathSerializer,
    LocationImageSerializer,
    SeriesLocationSerializer,
    LocationSeriesSerializer,
    SeriesLocationImagePathSerializer,
    SeriesLocationImageSerializer
)
from .models import Country, Prefecture, City, Series, Location, LocationImage, SeriesLocation, SeriesLocationImage

from Real2D.settings import BASE_DIR


def _get_locations_from_series(series_id):
    series_location_list = SeriesLocation.objects.filter(series=series_id).select_related()
    serialized_series_location_list = SeriesLocationSerializer(series_location_list, many=True)

    new_series_location_list = []

    for series_location in serialized_series_location_list.data:
        series_location['location']['location_images'] = _get_location_images(series_location['location']['id'])
        series_location['series_location_images'] = _get_series_location_images(series_location['id'])
        new_series_location_list.append(series_location)

    return new_series_location_list


def _get_series_from_location(location_id):
    series_list = SeriesLocation.objects.filter(location=location_id).select_related()
    serialized_series_list = LocationSeriesSerializer(series_list, many=True)
    return serialized_series_list.data


def _get_location_images(location_id):
    image_list = LocationImage.objects.filter(location=location_id)
    serialized_image_list = LocationImagePathSerializer(image_list, many=True)
    return serialized_image_list.data


def _get_series_location_images(series_location_id):
    image_list = SeriesLocationImage.objects.filter(id=series_location_id)
    serialized_image_list = SeriesLocationImagePathSerializer(image_list, many=True)
    return serialized_image_list.data


@api_view(['GET'])
def countries(request):
    country_list = Country.objects.all().order_by('name')
    serialized_country_list = CountrySerializer(country_list, many=True)
    return Response(serialized_country_list.data)


@api_view(['GET'])
def prefectures(request, country_id):
    prefecture_list = Prefecture.objects.filter(country=country_id).order_by('name')
    serialized_prefecture_list = PrefectureSerializer(prefecture_list, many=True)
    return Response(serialized_prefecture_list.data)


@api_view(['GET'])
def cities(request, prefecture_id):
    city_list = City.objects.filter(prefecture=prefecture_id).order_by('name')
    serialized_city_list = CitySerializer(city_list, many=True)
    return Response(serialized_city_list.data)


@api_view(['GET'])
def series(request):
    series_list = Series.objects.all().order_by('name')
    serialized_series_list = SeriesSerializer(series_list, many=True)
    return Response(serialized_series_list.data)


@api_view(['GET'])
def series_detail(request, series_id):
    try:
        series_item = Series.objects.get(id=series_id)
    except Series.DoesNotExist:
        return Response(status=404)

    serialized_series_item = SeriesSerializer(series_item)
    response_data = serialized_series_item.data
    response_data['locations'] = _get_locations_from_series(series_id)
    return Response(response_data)


@api_view(['GET'])
def locations(request):
    location_list = Location.objects.all()
    serialized_location_list = LocationSerializer(location_list, many=True)
    return Response(serialized_location_list.data)


@api_view(['GET'])
def location_detail(request, location_id):
    try:
        location_item = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return Response(status=404)

    serialized_location_item = LocationSerializer(location_item)
    response_data = serialized_location_item.data
    response_data['location_images'] = _get_location_images(location_id)
    response_data['series'] = _get_series_from_location(location_id)
    return Response(response_data)


@api_view(['GET'])
def cover_image(request, uuid):
    try:
        series_item = Series.objects.get(image_name=uuid)
    except Series.DoesNotExist:
        return HttpResponse(status=404)

    serialized_series_item = SeriesImageSerializer(series_item)
    image = serialized_series_item.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return HttpResponse(status=404)


@api_view(['GET'])
def location_image(request, uuid):
    try:
        location_image_item = LocationImage.objects.get(image_name=uuid)
    except LocationImage.DoesNotExist:
        return HttpResponse(status=404)

    serialized_location_image = LocationImageSerializer(location_image_item)
    image = serialized_location_image.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return HttpResponse(status=404)


@api_view(['GET'])
def series_location_image(request, uuid):
    try:
        series_location_image_item = SeriesLocationImage.objects.get(image_name=uuid)
    except SeriesLocationImage.DoesNotExist:
        return HttpResponse(status=404)

    serialized_series_location_image = SeriesLocationImageSerializer(series_location_image_item)
    image = serialized_series_location_image.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return HttpResponse(status=404)