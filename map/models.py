from django.db import models

class Station(models.Model):
    code = models.IntegerField()
    station_name = models.CharField(max_length=16)
    location_x = models.DecimalField(max_digits=9, decimal_places=6)
    location_y = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        ordering = ('station_name', 'code')
    def __str__(self):
        return self.station_name

class RealPassenger(models.Model):
    station = models.ForeignKey(Station)
    date = models.DateField()
    on_passenger = models.IntegerField()
    off_passenger = models.IntegerField()

    def get_date(self):
        return self.date

    def get_on_passenger(self):
        return self.on_passenger

    def get_off_passenger(self):
        return self.off_passenger

class ExpectatedPassenger(models.Model):
    station = models.ForeignKey(Station)
    date = models.DateTimeField()
    on_passenger = models.IntegerField()
    off_passenger = models.IntegerField()

    def get_date(self):
        return self.date

    def get_on_passenger(self):
        return self.on_passenger

    def get_off_passenger(self):
        return self.off_passenger