from django.contrib import admin

from .models import *


class ResidentialCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_valid')
    list_filter = ('is_valid',)
    search_fields = ('title',)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'star', 'country', 'state', 'city_or_section', 'phone_number', 'address',
                    'number_of_rooms', 'floors', 'capacity', 'is_valid')
    list_filter = ('country', 'is_valid')
    search_fields = ('name', 'country', 'state', 'city_or_section', 'is_valid')


class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'room_number', 'floor', 'area', 'capacity', 'single_beds',
                    'double_beds', 'extra_beds', 'is_valid',)
    list_filter = ('is_valid',)
    search_fields = ('hotels',)


class ResidentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'residential_category', 'name', 'country', 'state', 'city_or_section', 'phone_number',
                    'address', 'number_of_rooms', 'floors', 'capacity', 'is_valid')
    list_filter = ('residential_category', 'country', 'is_valid')
    search_fields = ('name', 'country', 'state', 'city_or_section', 'is_valid')


class HotelRoomFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'room', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'room')


admin.site.register(ResidentialCategory, ResidentialCategoryAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRoom, HotelRoomAdmin)
admin.site.register(Residential, ResidentialAdmin)
admin.site.register(HotelRoomFeature, HotelRoomFeatureAdmin)
