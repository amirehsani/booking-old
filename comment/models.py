from residence.models import *
from air.models import *
from abstract.models import AbstractComment


class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_comments')


class HotelRoomComment(AbstractComment):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_room_comments')


class ResidentialComment(AbstractComment):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='residential_comments')


class AirlineComment(AbstractComment):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airline_comments')


class AirportComment(AbstractComment):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airport_comments')
