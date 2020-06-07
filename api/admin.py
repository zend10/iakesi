from django.contrib import admin
from .models import Country, Prefecture, City, Series, Location, LocationImage, SeriesLocation, SeriesLocationImage


admin.site.register(Country)
admin.site.register(Prefecture)
admin.site.register(City)
admin.site.register(Series)
admin.site.register(Location)
admin.site.register(LocationImage)
admin.site.register(SeriesLocation)
admin.site.register(SeriesLocationImage)