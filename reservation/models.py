from django.db import models

from users.models import User
from residence.models import HotelRoom, Residential
from flight.models import FlightTicket


class HotelRoomReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING)
    number_of_guests = models.PositiveSmallIntegerField()


class ResidentialReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    residential = models.ForeignKey(Residential, on_delete=models.DO_NOTHING)
    number_of_guests = models.PositiveSmallIntegerField()


class FlightTicketReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    flight_ticket = models.ForeignKey(FlightTicket, on_delete=models.DO_NOTHING)
    number_of_passengers = models.PositiveSmallIntegerField()
