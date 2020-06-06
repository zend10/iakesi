import uuid
from django.db import models
from Real2D.settings import COVER_FOLDER, COVER_API_PATH


class Series(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, upload_to=COVER_FOLDER)
    image_name = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    description = models.TextField()
    anilist_id = models.IntegerField()
    last_modified = models.DateField(auto_now=True)

    def image_path(self):
        return f'{COVER_API_PATH}{self.image_name}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"


class Location(models.Model):
    name = models.CharField(max_length=300)
    remarks = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class SeriesLocation(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f'{self.series} - {self.location}'
