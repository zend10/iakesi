from rest_framework import serializers

from .models import *
from api.modules.series import SeriesSerializer
from api.modules.location import LocationSerializer


__all__ = [
    'SeriesLocationSerializer',
    'SeriesLocationImagePathSerializer',
    'SeriesLocationImageSerializer',
    'LocationSeriesSerializer'
]


class SeriesLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = SeriesLocation
        fields = ('id', 'location', 'remarks')


class SeriesLocationImagePathSerializer(serializers.ModelSerializer):
    series_location_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = SeriesLocationImage
        fields = ('series_location_image', 'remarks')


class SeriesLocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesLocationImage
        fields = ('image', 'remarks')


class LocationSeriesSerializer(serializers.ModelSerializer):
    series = SeriesSerializer(read_only=True)

    class Meta:
        model = SeriesLocation
        fields = ('id', 'series', 'remarks')
