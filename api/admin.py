from django.contrib import admin

from .modules.series.models import *
from .modules.location.models import *
from .modules.series_location.models import *

# Series
admin.site.register(Series)

# Location
admin.site.register(Country)
admin.site.register(Prefecture)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(LocationImage)

# Series Location
admin.site.register(SeriesLocation)
admin.site.register(SeriesLocationImage)
