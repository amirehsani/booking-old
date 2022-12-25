from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from .serializers import *


class HotelRoomReservationDisplay(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HotelRoomReservationSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return HotelRoomReservation.objects.filter(hotel_room__id=room_id).get()


class ResidentialReservationDisplay(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResidentialReservationSerializer

    def get_queryset(self):
        residential_id = self.kwargs['residential_id']
        return ResidentialReservation.objects.filter(residential__id=residential_id).get()


class FlightTicketReservationDisplay(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlightTicketReservationSerializer

    def get_queryset(self):
        ticket_id = self.kwargs['ticket_id']
        return FlightTicketReservation.obejcts.filter(flight_ticket__id=ticket_id).get()
