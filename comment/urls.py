from django.urls import path
from .views import *

urlpatterns = [
    path('hotel/comment/<str:hotel>', HotelCommentView.as_view(), name='Hotel Comment'),
    path('hotelroom/comment/<int:hotel_room_id>', HotelRoomCommentView.as_view(), name='Hotel Room Comment'),
    path('residential/comment/<str:residential>', ResidentialCommentView.as_view(), name='Residential Comment'),
    path('airline/comment/<str:airline>', AirlineCommentView.as_view(), name='Airline Comment'),
    path('airport/comment/<str:airport>', AirportCommentView.as_view(), name='Airport Comment'),
]
