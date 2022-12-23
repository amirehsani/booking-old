from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

admin.site.site_header = 'Booking Administration Panel'
admin.site.index_title = 'Feel free to take the wheel!'
