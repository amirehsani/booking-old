import json
import redis
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *

# from core.settings import DEFAULT_CACHE_TTL
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.views import APIView

''' Redis configuration for DRF views. '''
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_client_0 = redis.Redis(connection_pool=redis_pool, decode_responses=True)


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def airline_display(request):
#     if request.method == 'GET':
#         airline = redis_client_0.get('arline')
#
#         if airline is None:
#             print("Couldn't find data in cache, retrieving from database...")
#             airline = Airline.objects.all()
#             redis_client_0.setex('airline', 60 * 60 * 24 * 7, json.dumps(airline))
#
#         redis_client_0.get('airline')
#         serializer = AirlineSerializer(airline)
#         return Response(serializer.data)


class AirLineDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        airline = redis_client_0.get('arline')

        if airline is None:
            print("Couldn't find data in cache, retrieving from database...")
            airline = Airline.objects.all()
            redis_client_0.setex('airline', 60 * 60 * 24, json.dumps(airline))

        redis_client_0.get('airline')
        serializer = AirlineSerializer(airline)
        return Response(serializer.data)


class AirplaneDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        airplane = redis_client_0.get('airplane')

        if airplane is None:
            print("Couldn't find data in cache, retrieving from database...")
            airplane = Airplane.objects.all()
            redis_client_0.setex('airplane', 60 * 60 * 24, json.dumps(airplane))

        redis_client_0.get('airline')
        serializer = AirlineSerializer(airplane)
        return Response(serializer.data)


class AirportDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        airport = redis_client_0.get('airport')

        if airport is None:
            print("Couldn't find data in cache, retrieving from database...")
            airport = Airport.objects.all()
            redis_client_0.setex('airplane', 60 * 60 * 24, json.dumps(airport))

        redis_client_0.get('airline')
        serializer = AirlineSerializer(airport)
        return Response(serializer.data)
