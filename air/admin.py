from django.contrib import admin
from .models import Airport, Airline, Airplane


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'origin_country')
    list_filter = ('origin_country',)
    search_fields = ('name', 'origin_country')


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'register_number', 'number_of_seats')
    list_filter = ('manufacturer',)
    search_fields = ('manufacturer', 'name', 'register_number')


class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'city')
    list_filter = ('country', 'city')
    search_fields = ('country',)


# name of all model classes that we want to have a table of in our admin panel
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(Airport, AirportAdmin)
