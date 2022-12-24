from django.contrib import admin
from .models import UserCart


class UserCartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_username', 'cart_number', 'is_payed', 'get_hotel_room_reservation', 'get_residential_reservation',
        'get_flight_ticket_reservation', 'created_time', 'modified_time')
    list_filter = ('is_payed',)
    search_fields = ('get_username', 'is_payed', 'created_time', 'modified_time')

    @admin.display(description='User')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(description='Hotel Room Reservation')
    def get_hotel_room_reservation(self, obj):
        return obj.hotel_room_reservation.hotel_room.id

    @admin.display(description='Residential Reservation')
    def get_residential_reservation(self, obj):
        return obj.residential_reservation.residential.id

    @admin.display(description='Flight Ticket Reservation')
    def get_flight_ticket_reservation(self, obj):
        return obj.flight_ticket_reservation.flight.flight_number


admin.site.register(UserCart, UserCartAdmin)
