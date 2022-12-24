from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *


class FlightDisplay(ListAPIView):
    queryset = Flight.objects.all()
    permission_classes = [AllowAny]
    serializer_class = FlightSerializer


class FlightTicketDisplay(ListAPIView):
    queryset = FlightTicket.objects.all()
    permission_classes = [AllowAny]
    serializer_class = FlightTicketSerializer
