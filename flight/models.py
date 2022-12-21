from air.models import *


class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    duration = models.TimeField()
    start_time = models.DateTimeField()
    flight_class = None  # TODO Add
    seat_number = models.IntegerField()
    airplane_register_number = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    # TODO how to FK to a field of a model
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
