from django.shortcuts import render
from .models import Station, ExpectatedPassenger
from datetime import datetime

def display(request):
    station = Station.objects.all()
    expectatedPassenger = ExpectatedPassenger.objects.all()
    return render(request, 'map/display.html', {'station':station, 'expectatedPassenger':expectatedPassenger})
