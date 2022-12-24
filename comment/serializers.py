from rest_framework.serializers import ModelSerializer
from .models import *


class HotelCommentSerializer(ModelSerializer):
    class Meta:
        model = HotelComment
        fields = ['user', 'text', 'parent_comment', 'created_time']


class HotelRoomCommentSerializer(ModelSerializer):
    class Meta:
        model = HotelRoomComment
        fields = ['user', 'text', 'parent_comment', 'created_time']


class ResidentialCommentSerializer(ModelSerializer):
    class Meta:
        model = ResidentialComment
        fields = ['user', 'text', 'parent_comment', 'created_time']


class AirlineCommentSerializer(ModelSerializer):
    class Meta:
        model = AirlineComment
        fields = ['user', 'text', 'parent_comment', 'created_time']


class AirportCommentSerializer(ModelSerializer):
    class Meta:
        model = AirportComment
        fields = ['user', 'text', 'parent_comment', 'created_time']
