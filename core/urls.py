from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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

    # URL
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Simple JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

admin.site.site_header = 'Booking Administration Panel'
admin.site.index_title = 'Feel free to take the wheel!'
