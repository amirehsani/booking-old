from rest_framework.serializers import ModelSerializer

from flight.serializers import FlightTicketSerializer
from residence.serializers import HotelRoomSerializer, ResidentialSerializer
from .models import HotelRoomReservation, FlightTicketReservation, ResidentialReservation


class HotelRoomReservationSerializer(ModelSerializer):
    price_per_night = HotelRoomSerializer(many=True)
    hotel = HotelRoomSerializer(many=True)
    about = HotelRoomSerializer(many=True)
    address = HotelRoomSerializer(many=True)
    map_link = HotelRoomSerializer(many=True)
    phone_number = HotelRoomSerializer(many=True)

    class Meta:
        model = HotelRoomReservation
        fields = ['id', 'user', 'hotel_room', 'number_of_guests', 'checkin', 'checkout', 'count_of_nights',
                  'price_per_night', 'hotel', 'about', 'address', 'map_link', 'phone_number']
        # TODO add admin.display for fields that need


class ResidentialReservationSerializer(ModelSerializer):
    residential_category = ResidentialSerializer()

    class Meta:
        model = ResidentialReservation
        fields = ['id', 'user', 'residential_category', 'residential', 'number_of_guests', 'checkin', 'checkout']


class FlightTicketReservationSerializer(ModelSerializer):
    flight_class = FlightTicketSerializer(many=True)

    class Meta:
        model = FlightTicketReservation
        fields = ['user', 'number_of_passengers', 'flight_class']
