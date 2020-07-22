from rest_framework import serializers

from .models import *


__all__ = [
    'SeriesSerializer',
    'SeriesAccessCountSerializer',
    'SeriesImageSerializer'
]


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    cover_image = serializers.ReadOnlyField(source='image_path')

    class Meta:
        model = Series
        fields = ('id', 'name', 'cover_image', 'description', 'anilist_id', 'last_modified', 'slug')


class SeriesAccessCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'access_count')


class SeriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('image', )
