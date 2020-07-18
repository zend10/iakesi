import uuid

from django.db import models

from iakesi.settings import COVER_FOLDER, COVER_API_PATH


__all__ = ['Series']


class Series(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, upload_to=COVER_FOLDER)
    image_name = models.UUIDField(unique=True)
    description = models.TextField()
    anilist_id = models.IntegerField()
    last_modified = models.DateField(auto_now=True)
    access_count = models.BigIntegerField(default=0)

    def image_path(self):
        return f'{COVER_API_PATH}{self.image_name}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"
