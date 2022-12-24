from rest_framework.serializers import ModelSerializer

from .models import *


class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'flight_type', 'flight_number',
                  'start_time', 'duration', 'airport', 'airline', 'airplane']


class FlightTicketSerializer(ModelSerializer):
    class Meta:
        model = FlightTicket
        fields = ['flight', 'flight_class', 'price_for_one_passenger']
