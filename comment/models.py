from residence.models import *
from air.models import *
from abstract.models import AbstractComment


class HotelComment(AbstractComment):
    comment = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_comments')


class HotelRoomComment(AbstractComment):
    comment = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_room_comments')


class ResidentialComment(AbstractComment):
    comment = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='residential_comments')


class AirlineComment(AbstractComment):
    comment = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airline_comments')


class AirportComment(AbstractComment):
    comment = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airport_comments')
