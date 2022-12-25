from django.urls import path
from .views import *

urlpatterns = [
    path('hotel/rates', HotelRateDisplay.as_view(), name='Hotel Rates'),
    path('hotelroom/rates', HotelRoomRateDisplay.as_view(), name='Hotel Room Rates'),
    path('residential/rates', ResidentialRateDisplay.as_view(), name='Residential Rates'),
    path('airline/rates', AirlineRateDisplay.as_view(), name='Airline Rates'),
]
