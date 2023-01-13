from rest_framework.serializers import ModelSerializer
from rest_framework import filters

from .models import *


class ResidentialCategorySerializer(ModelSerializer):
    class Meta:
        model = ResidentialCategory
        fields = ['id', 'title', 'is_valid']


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'star', 'name', 'about', 'country', 'state', 'city_or_section', 'number_of_rooms', 'capacity']
        search_fields = ['star', 'abstracthotelorresidential__name', 'abstracthotelorresidential__country',
                         'abstracthotelorresidential__state', 'abstracthotelorresidential__city_or_section',
                         'abstracthotelorresidential__capacity']
        filter_backend = (filters.SearchFilter,)


class HotelRoomSerializer(ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ['id', 'hotel', 'room_number', 'floor', 'area', 'single_beds', 'double_beds', 'extra_beds',
                  'price_per_night']
        search_field = ['floor', 'capacity', 'price_per_night', 'single_beds', 'double_beds', 'extra_beds']
        filter_backend = (filters.SearchFilter,)


class ResidentialSerializer(ModelSerializer):
    class Meta:
        model = Residential
        fields = ['id', 'residential_category', 'price_per_night', 'name', 'about', 'country', 'state',
                  'city_or_section', 'number_of_rooms', 'floors', 'capacity', 'area']
        search_fields = ['price_per_night', 'abstracthotelorresidential__name', 'abstracthotelorresidential__country',
                         'abstracthotelorresidential__state', 'abstracthotelorresidential__city_or_section',
                         'abstracthotelorresidential__capacity']
        filter_backends = (filters.SearchFilter,)
