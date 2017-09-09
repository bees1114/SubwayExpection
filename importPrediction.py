import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SubwayExpectionWeb.settings")
django.setup()
from map.models import Station
FILE_DIR = 'D:/git/SubwayExpection/Data/'


station_list = []
with open(FILE_DIR + 'output_station.txt') as stations_file:
    input_station = stations_file.readlines()
    station = input_station[0]
    station = station.split()

    for st in station:
        st = st.strip('[')
        st = st.strip(',')
        st = st.strip(']')
        st = st[1:-1]
        station_list.append(st)

print(station_list.__len__())
with open(FILE_DIR + 'station.csv', "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1] not in station_list:
            continue
        else:
            station_list.remove(row[1])
        if row[0] == '\ufeff"전철역코드"':
            continue


        _, created = Station.objects.get_or_create(
            code=row[4],
            station_name=row[1],
            location_x=row[7],
            location_y=row[8]
        )
    print(station_list)