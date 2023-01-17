from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *


class ResidentialCategoryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = ResidentialCategory.objects.all()
    serializer_class = ResidentialCategorySerializer


class HotelDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRoomDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer


class Residential(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Residential.objects.all()
    serializer_class = ResidentialSerializer
