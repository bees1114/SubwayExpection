from django.shortcuts import render
from .models import Station, ExpectatedPassenger
from datetime import datetime, date, time
from django.utils import timezone
import pytz

def display(request):
    station = Station.objects.all()
    '''
    datetime_object = datetime(2017, 9, 1, 8, 30)
    pytz.timezone("Asia/Seoul").localize(datetime_object)
    '''
    start_date = datetime(2017, 9, 1, 12, 30)
    date_string = str(start_date.year) + "년 " + str(start_date.month) + "월 " + \
                  str(start_date.day) + "일 " + str(start_date.hour) + "시 기준"
    expectedPassenger = ExpectatedPassenger.objects.filter(date=start_date)

    return render(request, 'map/display.html', {'time': start_date, 'expectedPassenger': expectedPassenger})
