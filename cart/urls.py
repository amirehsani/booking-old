from django.urls import path
from .views import UserCartDisplay

urlpatterns = [

    path('cart/<str:username>', UserCartDisplay.as_view(), name='user_cart_display')

]

