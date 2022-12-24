from django.contrib import admin
from .models import *


@admin.register(HotelRoomReservation)
class HotelRoomReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'hotel_room', 'number_of_guests')
    search_fields = ('get_username',)

    @admin.display(description='User')
    def get_username(self, obj):
        return obj.user.username


@admin.register(ResidentialReservation)
class ResidentialReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'residential', 'number_of_guests')
    search_fields = ('get_username',)

    @admin.display(description='User')
    def get_username(self, obj):
        return obj.user.username


@admin.register(FlightTicketReservation)
class FlightTicketReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'flight_ticket', 'number_of_passengers')
    search_fields = ('get_username',)

    @admin.display(description='User')
    def get_username(self, obj):
        return obj.user.username


