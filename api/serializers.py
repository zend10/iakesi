from rest_framework import serializers
from .models import Country, Prefecture, City, Series, Location, LocationImage, SeriesLocation, SeriesLocationImage


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


class SeriesSerializer(serializers.ModelSerializer):
    cover_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = Series
        fields = ('id', 'name', 'cover_image', 'description', 'anilist_id', 'last_modified')


class SeriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('image', )


class LocationSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country_name')
    prefecture = serializers.ReadOnlyField(source='prefecture_name')
    city = serializers.ReadOnlyField(source='city_name')

    class Meta:
        model = Location
        fields = ('id', 'name', 'country', 'prefecture', 'city', 'remarks', 'latitude', 'longitude', 'last_modified')


class LocationImagePathSerializer(serializers.ModelSerializer):
    location_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = LocationImage
        fields = ('location_image', 'remarks')


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = ('image', )


class SeriesLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = SeriesLocation
        fields = ('id', 'location', 'remarks')


class LocationSeriesSerializer(serializers.ModelSerializer):
    series = SeriesSerializer(read_only=True)

    class Meta:
        model = SeriesLocation
        fields = ('id', 'series', 'remarks')


class SeriesLocationImagePathSerializer(serializers.ModelSerializer):
    series_location_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = SeriesLocationImage
        fields = ('series_location_image', 'remarks')


class SeriesLocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesLocationImage
        fields = ('image', 'remarks')
