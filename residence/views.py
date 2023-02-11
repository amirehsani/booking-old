from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import DEFAULT_CACHE_TTL
from .serializers import *


class ResidentialCategoryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = ResidentialCategory.objects.all()
    serializer_class = ResidentialCategorySerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HotelDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HotelRoomDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 1))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Residential(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Residential.objects.all()
    serializer_class = ResidentialSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
