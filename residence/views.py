import redis
import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import DEFAULT_CACHE_TTL
from .serializers import *

''' Redis configuration for DRF views. '''
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=1)
redis_client_1 = redis.Redis(connection_pool=redis_pool, decode_responses=True)


class ResidentialCategoryDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = ResidentialCategory.objects.all()
    serializer_class = ResidentialCategorySerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HotelDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        hotel = redis_client_1.get('hotel')

        if hotel is None:
            hotel = Hotel.objects.all()
            redis_client_1.setex('hotel', 60 * 60 * 24, json.dumps(hotel))

        redis_client_1.get('hotel')
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)


class HotelRoomDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        hotel_room = redis_client_1.get('hotel_room')

        if hotel_room is None:
            hotel_room = HotelRoom.objects.all()
            redis_client_1.setex('hotel_room', 60 * 60 * 24, json.dumps(hotel_room))

        redis_client_1.get('hotel_room')
        serializer = HotelRoomSerializer(hotel_room)
        return Response(serializer.data)


class Residential(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        residential = redis_client_1.get('residential')

        if residential is None:
            residential = Residential.objects.all()
            redis_client_1.setex('hotel', 60 * 60 * 24, json.dumps(residential))

        redis_client_1.get('residential')
        serializer = ResidentialSerializer(residential)
        return Response(serializer.data)
