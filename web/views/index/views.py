from django.shortcuts import render
from api.modules.series.handlers import get_popular_series
from api.modules.location.handlers import get_popular_locations

index_path = 'index/'


def index(request):
    popular_series = get_popular_series()['data']
    popular_location = get_popular_locations()['data']
    return render(request, f'{index_path}index.html', { 'popular_series': popular_series, 'popular_location': popular_location })
