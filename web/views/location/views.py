from django.http import HttpResponse
from django.shortcuts import render

from api.modules.location.handlers import get_location_detail


def detail(request, location_id):
    context = get_location_detail(location_id)
    return render(request, 'location/index.html', context)
