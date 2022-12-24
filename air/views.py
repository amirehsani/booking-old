from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from .serializers import *


class AirLineDisplay(ListAPIView):
    queryset = Airline.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AirlineSerializer


class AirplaneSerializer(ListAPIView):
    queryset = Airplane.objects.all()  # TODO only get each airplane model once
    permission_classes = [AllowAny]
    serializer_class = AirplaneSerializer


class AirportSerializer(ListAPIView):
    queryset = Airport.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AirportSerializer
