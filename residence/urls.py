from django.urls import path
from .views import *

urlpatterns = [
    path('residential_category', ResidentialCategoryDisplay.as_view(), name='Residential Categories')
]
