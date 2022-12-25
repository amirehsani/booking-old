from abstract.models import AbstractRate
from residence.models import HotelRoom, Residential, Hotel
from air.models import *


class HotelRate(AbstractRate):
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING,
                              related_name='hotel_rate', default=1)


class HotelRoomRate(AbstractRate):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING, related_name='hotel_room_rate', default=1)


class ResidentialRate(AbstractRate):
    residential = models.ForeignKey(Residential, on_delete=models.DO_NOTHING, default=1)


class AirlineRate(AbstractRate):
    airline = models.ForeignKey(Airline, on_delete=models.DO_NOTHING, default=1)
