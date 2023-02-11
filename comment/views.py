from rest_framework_simplejwt.authentication import JWTAuthentication

from abstract.permissions import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *

''' Not using caching due to high frequency and large number of comments in production.'''


class HotelCommentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelCommentSerializer

    def get_queryset(self):
        name = self.kwargs['hotel']
        return HotelComment.objects.filter(hotel__name=name, status='Approved').all()


class HotelRoomCommentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRoomCommentSerializer

    def get_queryset(self):
        id = self.kwargs['hotel_room_id']
        return HotelRoomComment.objects.filter(hotel_room__id=id, status='Approved').all()


class ResidentialCommentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResidentialCommentSerializer

    def get_queryset(self):
        name = self.kwargs['residential']
        return ResidentialComment.objects.filter(residential__name=name, status='Approved').all()


class AirlineCommentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirlineCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airline']
        return AirlineComment.objects.filter(airline__name=name, status='Approved').all()


class AirportCommentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirportCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airport']
        return AirportComment.objects.filter(airport__name=name, status='Approved').all()
