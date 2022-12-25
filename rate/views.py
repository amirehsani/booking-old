from rest_framework.generics import ListCreateAPIView
from .serializers import *
from abstract.permissions import *


class HotelRateDisplay(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRateSerializer

    def get_queryset(self):
        name = self.kwargs['hotel']
        return HotelRate.objects.filter(hotel__name=name)


class HotelRoomRateDisplay(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRoomRateSerializer

    def get_queryset(self):
        id = self.kwargs['hotel_room_id']
        return HotelRoomRate.objects.filter(hotel_room__id=id)


class ResidentialRateDisplay(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResidentialRateSerializer

    def get_queryset(self):
        name = self.kwargs['residential']
        return ResidentialRate.objects.filter(residential__name=name)


class AirlineRateDisplay(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirlineRateSerializer

    def get_queryset(self):
        name = self.kwargs['airline']
        return AirlineRate.objects.filter(airline__name=name)
