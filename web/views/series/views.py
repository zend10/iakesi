from django.shortcuts import render
from django.core.paginator import Paginator

from api.modules.series.handlers import get_series_detail, get_all_series


def detail(request, series_id):
    context = get_series_detail(series_id)
    return render(request, 'series/detail.html', context)


def lists(request):
    series_list = {}
    queryset = get_all_series()
    
    for series in queryset:
        first_char = series.name[0]
        if first_char not in series_list:
            series_list[first_char] = [series]
        else:
            series_list[first_char].append(series)
            
    context = {
        'data': series_list
    }
    return render(request, 'series/lists.html', context)
