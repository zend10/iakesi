from rest_framework import serializers
from .models import Series, Location, SeriesLocation


class SeriesSerializer(serializers.ModelSerializer):
    image_path = serializers.ReadOnlyField()

    class Meta:
        model = Series
        fields = ('id', 'name', 'image_path', 'description', 'anilist_id', 'last_modified')


class SeriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('image', )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'remarks', 'latitude', 'longitude', 'last_modified')


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
