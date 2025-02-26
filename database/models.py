from django.db import models
from postgres_copy import CopyManager
from django.utils.translation import gettext_lazy as _

class Stations(models.Model):
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))
    name = models.CharField(verbose_name=_('station name'), max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = _('station')
        verbose_name_plural = _('stations')

        indexes = [
            models.Index(feilds=['latitude', 'longitude'])
        ]

    def __str__(self):
        return f'{self.name} - E{self.longitude} N{self.latitude}'



class WeatherData(models.Model):
    station = models.ForeignKey(Stations, on_delete=models.CASCADE, verbose_name=_('station'))
    forecast_start = models.DateTimeField(verbose_name=_('date time(UTC)'))
    tfp = models.IntegerField(verbose_name=_('time from prediction'))
    T2 = models.FloatField(verbose_name=_('temperature(°C)'))
    wind_direction = models.IntegerField(verbose_name=_('wind direction(deg)'))
    wind_speed = models.FloatField(verbose_name=_('wind speed(m/s)'))
    Q2 = models.FloatField(verbose_name=_('#'))
    PSFC = models.FloatField(verbose_name=_('surface pressure(Pa)'))


    class Meta:
        indexes = [
            models.Index(fields=['station', 'forecast_start', 'tfp']),
        ]

    objects = CopyManager()

    def __str__(self):
        return f"station: {self.station} - time: {self.forecast_start}"          
