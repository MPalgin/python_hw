import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    list_of_stations = []
    with open(BUS_STATION_CSV, encoding='utf-8') as file:
        dict_with_data = csv.DictReader(file)
        for row in dict_with_data:
            list_of_stations.append({'Name': row.get('Name'), 'Street': row.get('Street'), 'District': row.get('District')})

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_of_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': list_of_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
