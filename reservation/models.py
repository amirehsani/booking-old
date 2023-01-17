from django.db import models

from abstract.models import AbstractReservation
from users.models import User
from residence.models import HotelRoom, Residential
from flight.models import FlightTicket


class HotelRoomReservation(AbstractReservation):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING)
    number_of_guests = models.PositiveSmallIntegerField()

    checkin = models.DateField(auto_now=True)
    checkout = models.DateField(auto_now=True)
    count_of_nights = models.PositiveIntegerField(default=1)


class ResidentialReservation(AbstractReservation):
    residential = models.ForeignKey(Residential, on_delete=models.DO_NOTHING)
    number_of_guests = models.PositiveSmallIntegerField()

    checkin = models.DateField(auto_now=True)
    checkout = models.DateField(auto_now=True)
    count_of_nights = models.PositiveIntegerField(default=1)


class FlightTicketReservation(AbstractReservation):
    flight_ticket = models.ForeignKey(FlightTicket, on_delete=models.DO_NOTHING)
    number_of_passengers = models.PositiveSmallIntegerField(default=1)
