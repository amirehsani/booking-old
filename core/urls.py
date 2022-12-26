from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('profile<str:username>', include('users.urls')),
    path('', include('rate.urls')),
    path('', include('comment.urls')),
    path('', include('users.urls')),
    path('', include('residence.urls')),
    path('', include('reservation.urls')),
    path('', include('cart.urls')),
]

admin.site.site_header = 'Booking Administration Panel'
admin.site.index_title = 'Feel free to take the wheel!'
