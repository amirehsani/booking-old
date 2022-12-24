from django.urls import path
from .views import *

urlpatterns = [
    path('profile<str:username>', user_profile_display, name='Profile')
]
