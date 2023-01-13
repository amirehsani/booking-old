from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.cache import cache

from .models import *
from users.models import User
from users.utils import send_otp_to_user


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'email', 'name', 'date_of_birth', 'nationality', 'id_number', 'created_time']


class LoginStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number',)
        extra_kwargs = {'phone_number': {'validators': []}}

    def create(self, validated_data):
        phone_number = validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            random_username = f'user_{phone_number}'
            user = User.objects.create_user(random_username, phone_number=phone_number)

        send_otp_to_user(user)

        return user


class LoginStep2Serializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'otp_code')
        extra_kwargs = {'phone_number': {'validators': [], 'write_only': True}}

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        otp = attrs['otp_code']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise ValidationError('Phone number does not exist')

        expected_otp = cache.get(f'otp_code:{user.phone_number}')
        if expected_otp != otp:
            raise ValidationError('The code you sent is invalid')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        return user
