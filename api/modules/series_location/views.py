from django.http import HttpResponse
from rest_framework.decorators import api_view

from .handlers import *


@api_view(['GET'])
def series_location_image(request, uuid):
    return HttpResponse(**get_series_location_image(uuid))