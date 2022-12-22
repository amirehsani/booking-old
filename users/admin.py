from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'nationality', 'date_of_birth', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user', 'first_name', 'last_name', 'nationality')
