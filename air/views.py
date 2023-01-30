import json
import redis
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import DEFAULT_CACHE_TTL
from .serializers import *


# WE'RE TESTING REDIS FOR OUR DJANGO VIEWS USING DRF FUNCTIONAL VIEWS.

redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=9)
redis_client_9 = redis.Redis(connection_pool=redis_pool, decode_responses=True)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def airline_display(request):
    if request.method == 'GET':
        airline = redis_client_9.get('arline')

        if airline is None:
            print("Couldn't find data in cache, retrieving from database...")
            airline = Airline.objects.all()
            redis_client_9.setex('airline', 60 * 60 * 24 * 7, json.dumps(airline))

        redis_client_9.get('airline')
        serializer = AirlineSerializer(airline)
        return Response(serializer.data)


# TODO Change the default view back to DRF CBV with caching capabilities.

# class AirLineDisplay(ListAPIView):
#     queryset = Airline.objects.all()
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     serializer_class = AirlineSerializer


class AirplaneDisplay(ListAPIView):
    queryset = Airplane.objects.all()  # TODO only get each airplane model once
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirplaneSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 2))  # TODO CHECK IF IT's CORRECT
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AirportDisplay(ListAPIView):
    queryset = Airport.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirportSerializer
