from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<str:username>/', ProfileDisplay.as_view(), name='Profile')
]
