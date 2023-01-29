import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from abstract.redis_client import redis_client0


# WE'RE TESTING REDIS FOR OUR DJANGO VIEWS USING DRF FUNCTIONAL VIEWS.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def airline_display(request):
    if request.method == 'GET':
        airline = redis_client0.get('arline')

        if airline is None:
            print("Couldn't find data in cache, retrieving from database...")
            airline = Airline.objects.all()
            redis_client0.setex('airline', 60*60*24*7, json.dumps(airline))

        redis_client0.get('airline')
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


class AirportDisplay(ListAPIView):
    queryset = Airport.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirportSerializer
