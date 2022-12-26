from django.urls import path
from .views import *

urlpatterns = [
    path('residentialgallery/<int:id>/', ResidentialGalleryDisplay.as_view(), name='Residential Gallery'),
    path('hotelroomgallery/<int:id>/', HotelRoomGalleryDisplay.as_view(), name='Hotel Room Gallery'),
    path('airportgallery/<it:id>/', AirportGalleryDisplay.as_view(), name='Airport Gallery'),
]
