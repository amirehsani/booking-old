from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *


class AirLineDisplay(ListAPIView):
    queryset = Airline.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AirlineSerializer


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
