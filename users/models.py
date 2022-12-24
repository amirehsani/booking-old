# import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.manager import BaseManager

# from reservation.models import *


class User(AbstractUser):
    phone_number = models.PositiveBigIntegerField(unique=True, null=True, blank=True, validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')])

    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)

    # REQUIRED_FIELDS and USERNAME_FIELD are already in AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/user_avatars/')
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')

    nationality = models.CharField(max_length=64, null=True, blank=True)
    id_number = models.PositiveIntegerField(default=11111111)

    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    unique_together = ['nationality', 'id_number']

    def __str__(self):
        return self.user.username


class CustomUserManager(BaseManager):
    pass  # TODO create custom manager


# class UserCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_cart')
#     cart_number = models.PositiveIntegerField(editable=False, default=uuid.uuid4)
#
#     hotel_room_reservation = models.ForeignKey(HotelRoomReservation, on_delete=models.DO_NOTHING,
#                                                verbose_name='Hotel Room Reservation')
#     residential_reservation = models.ForeignKey(ResidentialReservation, on_delete=models.DO_NOTHING,
#                                                 verbose_name='Residential Reservation')
#     flight_ticket_reservation = models.ForeignKey(FlightTicketReservation, on_delete=models.DO_NOTHING,
#                                                   verbose_name='Flight Ticket Reservation')
#
#     is_payed = models.BooleanField(default=True, verbose_name='Is payed')
#
#     created_time = models.DateTimeField(auto_now=True)
#     modified_time = models.DateTimeField(auto_now_add=True)
#
#     unique_together = ['user', 'cart_number']
