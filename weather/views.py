from django.http import JsonResponse
from django.shortcuts import render

from db import DataBase
from weather_api import Weather

db_client = DataBase("weather.db", 'weather')


def index(request):
    context = {}
    i = 1
    for item in db_client.get_cities():
        context["city" + str(i)] = item
        i += 1
    return render(request, 'weather/index.html', context)


def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        w = Weather(city)
        info = w.get_info()
        db_client.add_city(*info)
        data = {"message": "ok"}
        return JsonResponse(data)
