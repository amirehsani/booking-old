from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from .serializers import *


class HotelCommentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HotelCommentSerializer

    def get_queryset(self):
        name = self.kwargs['hotel']
        return HotelComment.objects.filter(hotel__name=name, status='Approved')


class HotelRoomCommentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HotelRoomCommentSerializer

    def get_queryset(self):
        id = self.kwargs['hotel_room_id']
        return HotelRoomComment.objects.filter(hotel_room__id=id, status='Approved')


class ResidentialCommentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ResidentialCommentSerializer

    def get_queryset(self):
        name = self.kwargs['residential']
        return ResidentialComment.objects.filter(residential__name=name, status='Approved')


class AirlineCommentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AirlineCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airline']
        return AirlineComment.objects.filter(airline__name=name, status='Approved')


class AirportCommentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AirportCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airport']
        return AirportComment.objects.filter(airport__name=name, status='Approved')
