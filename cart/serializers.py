from .models import UserCart
from rest_framework.serializers import ModelSerializer


class UserCartSerializer(ModelSerializer):
    class Meta:
        model = UserCart
        fields = ['user', 'cart_number', 'hotel_room_reservation', 'residential_reservation',
                  'flight_ticket_reservation', 'is_payed']
