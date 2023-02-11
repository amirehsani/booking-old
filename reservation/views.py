from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *


# TODO needs to be completed

class FlightReservationAPI(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FlightTicketReservationSerializer

    def get_queryset(self):
        flight_ticket = self.request.data.get('flight_ticket', )
        number_of_passengers = self.request.data.get('number_of_passengers', )


class ResidentialReservationAPI(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ResidentialReservationSerializer

    def get_queryset(self):
        residential = self.request.data.get('residential', )
        number_of_guests = self.request.data.get('number_of_guests', )
        checkin = self.request.data.get('checkin', )
        checkout = self.request.data.get('checkout', )
        count_of_nights = self.request.data.get('count_of_nights', )

        residential_reserved = ResidentialReservation.objects.filter(checkin=checkin, checkout=checkout)


class HotelRoomReservationAPI(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HotelRoomReservationSerializer

    def get_queryset(self):
        hotel_room = self.request.data.get('hotel_room', )
        number_of_guests = self.request.data.get('number_of_guests', )
        checkin = self.request.data.get('checkin', )
        checkout = self.request.data.get('checkout', )
        count_of_nights = self.request.data.get('count_of_nights', )

        residences_reserved = HotelRoomReservation.objects.filter(checkin=checkin, checkout=checkout)
