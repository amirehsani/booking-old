from rest_framework.serializers import ModelSerializer
from rest_framework import filters

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
        search_filters = ['flight_class', 'price_for_one_passenger', 'flight__origin', 'flight__destination',
                          'flight__start_time']
        filter_backend = (filters.SearchFilter,)
