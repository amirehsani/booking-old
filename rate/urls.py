from django.urls import path
from .views import *

urlpatterns = [
    path('hotel/rates/<str:hotel>/', HotelRateDisplay.as_view(), name='Hotel Rates'),
    path('hotelroom/rates/<int:hotel_room_id>/', HotelRoomRateDisplay.as_view(), name='Hotel Room Rates'),
    path('residential/rates/<str:airline>/', ResidentialRateDisplay.as_view(), name='Residential Rates'),
    path('airline/rates/<str:airport>/', AirlineRateDisplay.as_view(), name='Airline Rates'),
]
