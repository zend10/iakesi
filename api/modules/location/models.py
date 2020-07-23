import uuid

from django.db import models
from django.utils.text import slugify

from iakesi.settings import LOCATION_FOLDER, LOCATION_API_PATH


__all__ = ['Country', 'Prefecture', 'City', 'Location', 'LocationImage']


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


class Location(models.Model):
    name = models.CharField(max_length=300)
    alt_name = models.CharField(max_length=300, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(blank=True)
    source = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_modified = models.DateField(auto_now=True)
    access_count = models.BigIntegerField(default=0)

    def country_name(self):
        return self.country.name

    def prefecture_name(self):
        return self.prefecture.name

    def city_name(self):
        return self.city.name

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


class LocationImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=LOCATION_FOLDER)
    image_name = models.UUIDField(unique=True)
    remarks = models.TextField(blank=True)

    def image_path(self):
        return f'{LOCATION_API_PATH}{self.image_name}'

    def __str__(self):
        return f'{self.location} - {self.image_name}'

    class Meta:
        verbose_name = "Location Image"
        verbose_name_plural = "Location Images"


