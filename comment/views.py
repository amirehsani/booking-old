from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from .serializers import *


class HotelCommentView(ListCreateAPIView):
    queryset = HotelComment.objects.filter(hotel=Hotel.name, status='Approved')  # TODO is it correct ?
    permission_classes = [AllowAny]
    serializer_class = HotelCommentSerializer


class HotelRoomCommentView(ListCreateAPIView):
    queryset = HotelRoomComment.objects.filter(hotel_room_id=HotelRoom.id, status='Approved')
    permission_classes = [AllowAny]
    serializer_class = HotelRoomCommentSerializer


class ResidentialCommentView(ListCreateAPIView):
    queryset = ResidentialComment.objects.filter(residential=Residential.name, status='Approved')
    permission_classes = [AllowAny]
    serializer_class = ResidentialCommentSerializer


class AirlineCommentView(ListCreateAPIView):
    queryset = AirlineComment.objects.filter(airline=Airline.name, status='Approved')
    permission_classes = [AllowAny]
    serializer_class = AirlineCommentSerializer


class AirportCommentView(ListCreateAPIView):
    queryset = AirportComment.objects.filter(airport=Airline.name, status='Approved')
    permission_classes = [AllowAny]
    serializer_class = AirportCommentSerializer
