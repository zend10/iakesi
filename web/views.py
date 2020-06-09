from django.http import HttpResponse
from django.shortcuts import render

from api.modules.series.handlers import *





def series(request, series_id):
    context = get_series_detail(series_id)
    return render(request, 'series/index.html', context)
