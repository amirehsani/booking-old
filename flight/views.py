import json
import redis

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *

''' Redis configuration for DRF views. '''
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=1)
redis_client_1 = redis.Redis(connection_pool=redis_pool, decode_responses=True)


class FlightDisplay(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        flight = redis_client_1.get('flight')

        if flight is None:
            flight = Flight.objects.all()
            redis_client_1.setex('flight', 60 * 60, json.dumps(flight))

        redis_client_1.get('flight')
        serializer = FlightSerializer
        return Response(serializer.data)


class FlightTicketDisplay(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, *args, **kwargs):
        flight_ticket = redis_client_1.get('flight_ticket')

        if flight_ticket is None:
            flight_ticket = FlightTicket.objects.all()
            redis_client_1.setex('flight_ticket', 60 * 60, json.dumps(flight_ticket))

        redis_client_1.get('flight_ticket')
        serializer = FlightTicketSerializer
        return Response(serializer.data)
