from django.urls import path
from .views import *

urlpatterns = [
    path('airlines/', AirLineDisplay.as_view(), name='Airlines List')
]
