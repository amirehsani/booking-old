from rest_framework.serializers import ModelSerializer

from .models import *


class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name', 'origin_country', 'about']


class AirplaneSerializer(ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['manufacturer', 'name', 'number_of_seats']


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = ['name', 'country', 'city']
