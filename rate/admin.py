from django.contrib import admin
from .models import *


class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rate', 'created_time', 'modified_time')
    search_fields = ('user',)


admin.site.register(HotelRate, RateAdmin)
admin.site.register(HotelRoomRate, RateAdmin)
admin.site.register(ResidentialRate, RateAdmin)
