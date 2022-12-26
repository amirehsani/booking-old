from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *


# TODO should Image APIs be created too ?

class ResidentialGalleryDisplay(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResidentialGallerySerializer
    queryset = ResidentialGallery.objects.filter(id=id).get()


class HotelRoomGalleryDisplay(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelRoomGallerySerializer
    queryset = HotelRoomGallery.objects.filter(id=id).get()


class AirportGalleryDisplay(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AirportGallerySerializer
    queryset = AirportGallery.objects.filter(id=id).get()
