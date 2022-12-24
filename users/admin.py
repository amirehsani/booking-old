from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number',
                    'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'name', 'nationality', 'id_number', 'date_of_birth', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('get_username', 'name', 'nationality', 'id_number')

    @admin.display(description='User')
    def get_username(self, obj):
        return obj.user.username


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

