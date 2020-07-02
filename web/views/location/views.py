from django.http import HttpResponse
from django.shortcuts import render

from Real2D.settings import GOOGLE_API_KEY
from api.modules.location.handlers import get_location_detail


def detail(request, location_id):
    context = get_location_detail(location_id)['data']
    return render(request, 'location/index.html', { 'data': context, 'apikey': GOOGLE_API_KEY })
