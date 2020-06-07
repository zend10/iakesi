import uuid

from django.db import models
from Real2D.settings import COVER_FOLDER, LOCATION_FOLDER, SERIES_FOLDER, COVER_API_PATH, LOCATION_API_PATH, SERIES_API_PATH


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Prefecture(models.Model):
    """
    Prefecture or Province or State
    """
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    """
    City or Town or Village
    """
    name = models.CharField(max_length=50)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


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
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_modified = models.DateField(auto_now=True)

    def country_name(self):
        return self.country.name

    def prefecture_name(self):
        return self.prefecture.name

    def city_name(self):
        return self.city.name

    def __str__(self):
        return self.name


class LocationImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=LOCATION_FOLDER)
    image_name = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    remarks = models.TextField(blank=True)

    def image_path(self):
        return f'{LOCATION_API_PATH}{self.image_name}'

    def __str__(self):
        return f'{self.location} - {self.image_name}'

    class Meta:
        verbose_name = "Location Image"
        verbose_name_plural = "Location Images"


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
