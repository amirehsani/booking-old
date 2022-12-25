from rest_framework.serializers import ModelSerializer
from .models import HotelRoomReservation, FlightTicketReservation, ResidentialReservation


class HotelRoomReservationSerializer(ModelSerializer):
    class Meta:
        model = HotelRoomReservation
        fields = ['id', 'user', 'hotel_room', 'number_of_guests', 'checkin', 'checkout', 'count_of_nights',
                  'price_per_night', 'hotel', 'about', 'address', 'map_link', 'phone_number']
        # TODO add admin.display for fields that need


class ResidentialReservationSerializer(ModelSerializer):
    class Meta:
        model = ResidentialReservation
        fields = ['id', 'user', 'residential_category', 'residential', 'number_of_guests', 'checkin', 'checkout',
                  'name', 'about', 'address', 'map_link', 'phone_number']


class FlightTicketReservationSerializer(ModelSerializer):
    class Meta:
        model = FlightTicketReservation
        fields = ['user', 'number_of_passengers', 'flight_class', 'price_for_one_passenger', 'origin', 'destination',
                  'flight_number', 'flight_type', 'start_time', 'duration', 'capacity', 'airport', 'airline',
                  'airplane']
