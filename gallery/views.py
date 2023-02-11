import json
import redis

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *

''' High priority task, will use caching'''
''' Redis configuration for DRF views. '''
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=2)
redis_client_2 = redis.Redis(connection_pool=redis_pool, decode_responses=True)


class ResidentialGalleryDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        residential_gallery = redis_client_2.get('residential_gallery')

        if residential_gallery is None:
            residential_gallery = ResidentialGallery.objects.all()
            redis_client_2.setex('airline', 60 * 60 * 24, json.dumps(residential_gallery))

        redis_client_2.get('airline')
        serializer = ResidentialGallerySerializer(residential_gallery)
        return Response(serializer.data)


class HotelRoomGalleryDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        hotel_room_gallery = redis_client_2.get('hotel_room_gallery')

        if hotel_room_gallery is None:
            hotel_room_gallery = HotelRoomGallery.objects.all()
            redis_client_2.setex('airline', 60 * 60 * 24, json.dumps(hotel_room_gallery))

        redis_client_2.get('airline')
        serializer = HotelRoomGallerySerializer(hotel_room_gallery)
        return Response(serializer.data)


class AirportGalleryDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        airport_gallery = redis_client_2.get('airport_gallery')

        if airport_gallery is None:
            airport_gallery = AirportGallery.objects.all()
            redis_client_2.setex('airline', 60 * 60 * 24, json.dumps(airport_gallery))

        redis_client_2.get('airline')
        serializer = AirportGallerySerializer(airport_gallery)
        return Response(serializer.data)
