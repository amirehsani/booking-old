from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import DEFAULT_CACHE_TTL
from .serializers import *
from .models import *

''' High priority task, will use caching'''


class ResidentialGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ResidentialGallerySerializer
    queryset = ResidentialGallery.objects.filter(id=id).get()

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HotelRoomGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = HotelRoomGallerySerializer
    queryset = HotelRoomGallery.objects.filter(id=id).get()

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AirportGalleryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirportGallerySerializer
    queryset = AirportGallery.objects.filter(id=id).get()

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
