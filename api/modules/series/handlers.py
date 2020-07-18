import os

from .models import *
from .serializers import *

from iakesi.settings import BASE_DIR
from api.commons.services import get_locations_from_series


__all__ = ['get_all_series', 'get_series_detail', 'get_cover_image', 'get_popular_series']


def get_all_series():
    return Series.objects.all().order_by('name')


def get_series_detail(series_id):
    try:
        series_item = Series.objects.get(id=series_id)
    except Series.DoesNotExist:
        return dict(status=404)

    # handle update access count
    temp_data = SeriesAccessCountSerializer(series_item).data
    temp_data['access_count'] = temp_data['access_count'] + 1
    update_serializer = SeriesAccessCountSerializer(series_item, data=temp_data)

    if update_serializer.is_valid():
        update_serializer.save()

    # retrieve additional detail
    serialized_series_item = SeriesSerializer(series_item)
    response_data = serialized_series_item.data
    response_data['locations'] = get_locations_from_series(series_id)
    return dict(data=response_data)


def get_cover_image(uuid):
    try:
        series_item = Series.objects.get(image_name=uuid)
    except Series.DoesNotExist:
        return dict(status=404)

    serialized_series_item = SeriesImageSerializer(series_item)
    image = serialized_series_item.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return dict(content=f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return dict(status=404)


def get_popular_series():
    series_list = Series.objects.all().order_by('-access_count')[:6]
    serialized_series_list = SeriesSerializer(series_list, many=True)
    return dict(data=serialized_series_list.data)