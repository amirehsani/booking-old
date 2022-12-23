from django.contrib import admin
from .models import *


class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'flight_number', 'flight_type', 'start_time',
                    'duration', 'capacity', 'get_airport_name', 'get_airline_name', 'get_airplane_register_number',)

    # this does the job or replacing 'airplane' ForeignKey with models.airplane.register_number
    @admin.display(description='Airplane')
    def get_airplane_register_number(self, obj):
        return obj.airplane.register_number

    @admin.display(description='Airline')
    def get_airline_name(self, obj):
        return obj.airline.name

    @admin.display(description='Airport')
    def get_airport_name(self, obj):
        return obj.airport.name


class FlightTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_flight_number', 'flight_class')
    list_filter = ('flight_class',)
    search_fields = ('get_flight_number',)

    @admin.display(description='Flight')
    def get_flight_number(self, obj):
        return obj.flight.flight_number


admin.site.register(Flight, FlightAdmin)
admin.site.register(FlightTicket, FlightTicketAdmin)
