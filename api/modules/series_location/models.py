import uuid

from django.db import models

from Real2D.settings import SERIES_FOLDER, SERIES_API_PATH
from api.modules.series import Series
from api.modules.location import Location


__all__ = ['SeriesLocation', 'SeriesLocationImage']


class SeriesLocation(models.Model):
    """
    Map series with location
    """
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f'{self.series} - {self.location}'

    class Meta:
        verbose_name = "Series Location"
        verbose_name_plural = "Series Locations"


class SeriesLocationImage(models.Model):
    series_location = models.ForeignKey(SeriesLocation, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=SERIES_FOLDER)
    image_name = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    remarks = models.TextField(blank=True)

    def image_path(self):
        return f'{SERIES_API_PATH}{self.image_name}'

    def __str__(self):
        return f'{self.series_location} - {self.image_name}'

    class Meta:
        verbose_name = "Series Location Image"
        verbose_name_plural = "Series Location Images"
