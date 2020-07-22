from rest_framework import serializers

from .models import *


__all__ = [
    'CountrySerializer',
    'PrefectureSerializer',
    'CitySerializer',
    'LocationSerializer',
    'LocationAccessCountSerializer',
    'LocationImagePathSerializer',
    'LocationImageSerializer'
]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefecture
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source='country_name')
    prefecture = serializers.ReadOnlyField(source='prefecture_name')
    city = serializers.ReadOnlyField(source='city_name')

    class Meta:
        model = Location
        fields = ('id', 'name', 'country', 'prefecture', 'city', 'remarks', 'latitude', 'longitude', 'last_modified', 'slug')


class LocationAccessCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'access_count')


class LocationImagePathSerializer(serializers.ModelSerializer):
    location_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = LocationImage
        fields = ('location_image', 'remarks')


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = ('image', )
