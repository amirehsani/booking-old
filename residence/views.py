from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import *


class ResidentialCategoryDisplay(ListAPIView):
    permission_classes = [AllowAny]
    queryset = ResidentialCategory.objects.all()
    serializer_class = ResidentialCategorySerializer


class HotelDisplay(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRoomDisplay(ListAPIView):
    permission_classes = [AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer


class Residential(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Residential.objects.all()
    serializer_class = ResidentialSerializer
