from rest_framework.serializers import ModelSerializer
from .models import *


class ResidentialGallerySerializer(ModelSerializer):
    class Meta:
        model = ResidentialGallery
        fields = ['id']


class HotelRoomGallerySerializer(ModelSerializer):
    class Meta:
        model = HotelRoomGallery
        fields = ['id']


class AirportGallerySerializer(ModelSerializer):
    class Meta:
        model = AirportGallery
        fields = ['id']


class ResidentialImageSerializer(ModelSerializer):
    class Meta:
        model = ResidentialImage
        fields = ['id', 'image', 'gallery']


class HotelRoomImageSerializer(ModelSerializer):
    class Meta:
        model = HotelRoomImage
        fields = ['id', 'image', 'gallery']


class AirportImageSerializer(ModelSerializer):
    class Meta:
        model = AirportImage
        fields = ['id', 'image', 'gallery']
