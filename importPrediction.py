import csv
import django
import os
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SubwayExpectionWeb.settings")
django.setup()
from map.models import ExpectatedPassenger
from map.models import Station
FILE_DIR = 'D:\git\SubwayExpection\Data'

station_list = []
with open(FILE_DIR + '\output_station.txt') as stations_file:
    input_station = stations_file.readlines()
    station = input_station[0]
    station = station.split()

    for st in station:
        st = st.strip('[')
        st = st.strip(',')
        st = st.strip(']')
        st = st[1:-1]
        station_list.append(st)
    station_list.sort()
    print(station_list)

hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(station_list.__len__())
with open('test_input_on_web.csv', "r",  encoding='utf-8') as file:
    reader = csv.reader(file)
    for row, hour in zip(reader, hours):
        for station, i in zip(station_list, range(station_list.__len__())):
            row[i] = row[i].replace(u'\ufeff', '')
            _, created = ExpectatedPassenger.objects.get_or_create(
                station=Station.objects.get(station_name=station),
                date=datetime(year=2017, month=9, day=1, hour=hour, minute=30),
                on_passenger=-1,
                off_passenger_1=row[i],
                off_passenger_2=row[i + 110],
                off_passenger_3=row[i + 220],
            )
    print(station_list)
