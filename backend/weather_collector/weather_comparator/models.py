from django.db import models

class Weather_history(models.Model):
    measure_id = models.PositiveBigIntegerField()
    datetime = models.DateTimeField(auto_now=False)
    min_temp = models.DecimalField(max_digits=7, decimal_places=3)
    max_temp = models.DecimalField(max_digits=7, decimal_places=3)
    the_temp = models.DecimalField(max_digits=7, decimal_places=3)
    humidity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.id) if self.id else ''
