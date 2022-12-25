from .models import *
from rest_framework.serializers import ModelSerializer


class HotelRateSerializer(ModelSerializer):
    class Meta:
        model = HotelRate
        fields = ['hotel', 'user', 'rate', 'created_time', 'modified_time']


class HotelRoomRateSerializer(ModelSerializer):
    class Meta:
        model = HotelRoomRate
        fields = ['hotel_room', 'user', 'rate', 'created_time', 'modified_time']


class ResidentialRateSerializer(ModelSerializer):
    class Meta:
        model = ResidentialRate
        fields = ['residential', 'user', 'rate', 'created_time', 'modified_time']


class AirlineRateSerializer(ModelSerializer):
    class Meta:
        model = AirlineRate
        fields = ['airline', 'user', 'rate', 'created_time', 'modified_time']
