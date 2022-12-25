from django.urls import path
from .views import *

urlpatterns = [

    path('hotelroomreservation/<int:room_id>/', HotelRoomReservationDisplay.as_view(),
         name='Hotel Room Reservation'),
    path('residentialreservation/<int:residential_id>/', ResidentialReservationDisplay.as_view(),
         name='Residential Reservation'),
    path('flightticketreservation/<int:ticket_id>/', FlightTicketReservationDisplay.as_view(),
         name='Flight Ticket Reservation'),
]
