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
    time = 12
    start_date = datetime(2017, 9, 1, time, 30)
    end_date = datetime(2017, 9, 1, time+2, 30)
    expectedPassenger = ExpectatedPassenger.objects.filter(date__range=(start_date, end_date))
    expectatedPassenger_1 = ExpectatedPassenger.objects.filter(date=start_date)
    expectatedPassenger_2 = ExpectatedPassenger.objects.filter(date=datetime(2017, 9, 1, time + 1, 30))
    expectatedPassenger_3 = ExpectatedPassenger.objects.filter(date=datetime(2017, 9, 1, time + 2, 30))

    return render(request, 'map/display.html', {'expectedPassenger': expectedPassenger,
                                                'expectatedPassenger_1': expectatedPassenger_1,
                                                'expectatedPassenger_2': expectatedPassenger_2,
                                                'expectatedPassenger_3': expectatedPassenger_3})
