from django.db import models
from abstract.models import AbstractRate
from residence.models import HotelRoom, Residential, Hotel


class HotelRate(AbstractRate):
    rate = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING,
                             related_name='hotel_rate')


class HotelRoomRate(AbstractRate):
    rate = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING, related_name='hotel_room_rate')


class ResidentialRate(AbstractRate):
    rate = models.ForeignKey(Residential, on_delete=models.DO_NOTHING)
