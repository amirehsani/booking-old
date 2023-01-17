from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *


class ResidentialGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ResidentialGallerySerializer
    queryset = ResidentialGallery.objects.filter(id=id).get()


class HotelRoomGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = HotelRoomGallerySerializer
    queryset = HotelRoomGallery.objects.filter(id=id).get()


class AirportGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirportGallerySerializer
    queryset = AirportGallery.objects.filter(id=id).get()
