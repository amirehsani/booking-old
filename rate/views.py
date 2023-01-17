from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from abstract.permissions import *


class HotelRateDisplay(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRateSerializer

    def get_queryset(self):
        name = self.kwargs['hotel']
        return HotelRate.objects.filter(hotel__name=name).all()


class HotelRoomRateDisplay(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRoomRateSerializer

    def get_queryset(self):
        id = self.kwargs['hotel_room_id']
        return HotelRoomRate.objects.filter(hotel_room__id=id).all()


class ResidentialRateDisplay(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResidentialRateSerializer

    def get_queryset(self):
        name = self.kwargs['residential']
        return ResidentialRate.objects.filter(residential__name=name).all()


class AirlineRateDisplay(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirlineRateSerializer

    def get_queryset(self):
        name = self.kwargs['airline']
        return AirlineRate.objects.filter(airline__name=name).all()
