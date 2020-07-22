from django.http import HttpResponse
from django.shortcuts import render

from iakesi.settings import GOOGLE_API_KEY
from api.modules.location.handlers import get_location_detail, get_all_locations


def detail(request, location_id, slug=None):
    context = get_location_detail(location_id)
    if (context.get('status') == 404):
        return render(request, 'base/404.html')
    else:
        return render(request, 'location/detail.html', { 'data': context['data'], 'apikey': GOOGLE_API_KEY })


def lists(request):
    location_list = {}
    queryset = get_all_locations()

    for location in queryset:
        country = location.country
        prefecture = location.prefecture
        city = location.city

        if country not in location_list:
            city = {city: [location]}
            prefecture = {prefecture: city}
            location_list[country] = prefecture
        elif prefecture not in location_list[country]:
            city = {city: [location]}
            location_list[country][prefecture] = city
        elif city not in location_list[country][prefecture]:
            location_list[country][prefecture][city] = [location]
        else:
            location_list[country][prefecture][city].append(location)

    context = {
        'data': location_list
    }
    return render(request, 'location/lists.html', context)