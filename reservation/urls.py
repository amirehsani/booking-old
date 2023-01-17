from django.urls import path
from .views import *

urlpatterns = [

    path('hotelroomreservation/<int:room_id>/', HotelRoomReservationAPI.as_view(),
         name='Hotel Room Reservation'),
    path('residentialreservation/<int:residential_id>/', ResidentialReservationAPI.as_view(),
         name='Residential Reservation'),
    path('flightticketreservation/<int:ticket_id>/', FlightReservationAPI.as_view(),
         name='Flight Ticket Reservation'),
]
