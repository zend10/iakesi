import os

from .models import *
from .serializers import *

from Real2D.settings import BASE_DIR


__all__ = ['get_series_location_image']


def get_series_location_image(uuid):
    try:
        series_location_image_item = SeriesLocationImage.objects.get(image_name=uuid)
    except SeriesLocationImage.DoesNotExist:
        return dict(status=404)

    serialized_series_location_image = SeriesLocationImageSerializer(series_location_image_item)
    image = serialized_series_location_image.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return dict(content=f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return dict(status=404)
