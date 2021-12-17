from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from weather_comparator.metaweather import Metaweather
import datetime
import socket
import os

def index(request):
    m = Metaweather()
    distinct_days = m.get_distinct_days()
    server_ip = socket.gethostbyname(socket.gethostname())
    return render(request, 'weather_comparator/index.html', {'title':'Data from DataBase', 'server_ip':server_ip, 'distinct_days':distinct_days})

def weather(request, year, month, day):
    rquested_date = f'{year}-{month}-{day}'
    dt_date = datetime.datetime.strptime(rquested_date, '%Y-%m-%d')
    if dt_date.date() == datetime.datetime.now().date():
        dt_date = dt_date - datetime.timedelta(days=1)
    year_ago_dt_date = dt_date - datetime.timedelta(days=365)
    m = Metaweather()

    try:
        req_date_data = m.get_weather_history('St Petersburg', dt_date)
    except Exception as e:
        return render(request, 'weather_comparator/error.html', {'title':'Error', 'exception_text':str(e)})

    try:
        year_ago_date_data = m.get_weather_history('St Petersburg', year_ago_dt_date)
    except Exception as e:
        return render(request, 'weather_comparator/error.html', {'title':'Error', 'exception_text':str(e)})

    title = f'The weather in Saint Petersburg at {dt_date.date().strftime("%d.%m.%Y")} and {year_ago_dt_date.date().strftime("%d.%m.%Y")}'

    diffs = {'min_temp': round(req_date_data['avg_data']['min_temp'] - year_ago_date_data['avg_data']['min_temp'], 3),
             'max_temp': round(req_date_data['avg_data']['max_temp'] - year_ago_date_data['avg_data']['max_temp'], 3),
             'the_temp': round(req_date_data['avg_data']['the_temp'] - year_ago_date_data['avg_data']['the_temp'], 3),
             'humidity': round(req_date_data['avg_data']['humidity'] - year_ago_date_data['avg_data']['humidity'], 3),
             }
    server_ip = socket.gethostbyname(socket.gethostname())
    return render(request, 'weather_comparator/weather.html', {'title': title,
                                                               'server_ip':server_ip,
                                                               'date': dt_date.date(),
                                                               'year_ago_date':year_ago_dt_date.date(),
                                                               'req_date_data':req_date_data,
                                                               'year_ago_date_data':year_ago_date_data,
                                                               'diffs': diffs,
                                                               })


def erase_db(request):
    m = Metaweather()
    m.erase_db()
    return redirect(index)


def delete_data(request, year, month, day):
    rquested_date = f'{year}-{month}-{day}'
    dt_date = datetime.datetime.strptime(rquested_date, '%Y-%m-%d')
    m = Metaweather()
    m.delete_data(dt_date)
    return redirect(index)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Page 404!")
