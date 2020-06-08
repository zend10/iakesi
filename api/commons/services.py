from api.modules.location import LocationImage, LocationImagePathSerializer
from api.modules.series_location import (
    SeriesLocation,
    SeriesLocationImage,
    SeriesLocationSerializer,
    SeriesLocationImagePathSerializer,
    LocationSeriesSerializer
)


def get_location_images(location_id):
    image_list = LocationImage.objects.filter(location=location_id)
    serialized_image_list = LocationImagePathSerializer(image_list, many=True)
    return serialized_image_list.data


def get_locations_from_series(series_id):
    series_location_list = SeriesLocation.objects.filter(series=series_id).select_related()
    serialized_series_location_list = SeriesLocationSerializer(series_location_list, many=True)

    new_series_location_list = []

    for series_location in serialized_series_location_list.data:
        series_location['location']['location_images'] = get_location_images(series_location['location']['id'])
        series_location['series_location_images'] = get_series_location_images(series_location['id'])
        new_series_location_list.append(series_location)

    return new_series_location_list


def get_series_location_images(series_location_id):
    image_list = SeriesLocationImage.objects.filter(id=series_location_id)
    serialized_image_list = SeriesLocationImagePathSerializer(image_list, many=True)
    return serialized_image_list.data


def get_series_from_location(location_id):
    series_list = SeriesLocation.objects.filter(location=location_id).select_related()
    serialized_series_list = LocationSeriesSerializer(series_list, many=True)
    return serialized_series_list.data