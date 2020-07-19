from django.shortcuts import render
from api.modules.series.handlers import get_popular_series
from api.modules.location.handlers import get_popular_locations


def index(request):
    popular_series = get_popular_series()['data']
    popular_locations = get_popular_locations()['data']
    return render(request, 'index/index.html', { 'popular_series': popular_series, 'popular_locations': popular_locations })
