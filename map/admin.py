from django.contrib import admin
from .models import Station, ExpectatedPassenger, RealPassenger

admin.site.register(Station)
admin.site.register(ExpectatedPassenger)
admin.site.register(RealPassenger)