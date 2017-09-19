from django.shortcuts import render
from .models import Station, ExpectatedPassenger
from datetime import datetime, date, time
from django.utils import timezone
import pytz

def display(request):
    start_date = datetime(2017, 9, 1, 12, 30)
    date_string = str(start_date.year) + "년 " + str(start_date.month) + "월 " + \
                  str(start_date.day) + "일 " + str(start_date.hour) + "시 기준"

    if request.method == 'GET':
        try:
            station_name = request.GET['station_name']
            searched_station = Station.objects.get(station_name=station_name)
            station_expectedPassenger = ExpectatedPassenger.objects.get(station=searched_station, date=start_date)
        except:
            station_expectedPassenger = None

    '''
    datetime_object = datetime(2017, 9, 1, 8, 30)
    pytz.timezone("Asia/Seoul").localize(datetime_object)
    '''
    expectedPassenger = ExpectatedPassenger.objects.filter(date=start_date)

    return render(request, 'map/display.html', {
        'time': start_date,
        'expectedPassenger': expectedPassenger,
        'searched_expectedPassenger': station_expectedPassenger,
    })
