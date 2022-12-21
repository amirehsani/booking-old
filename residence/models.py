from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from comment.models import AbstractComment


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    # location = models.PointField(geography=True, spatial_index=True)  # TODO import
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city_or_section = models.CharField(max_length=100)
    capacity = models.IntegerField()
    number_of_rooms = models.IntegerField()
    floors = models.IntegerField()
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    rate = None  # TODO add
    is_valid = models.BooleanField(default=True)


class HotelRoom(models.Model):
    room_number = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    bed = models.PositiveSmallIntegerField()
    extra_bed = models.PositiveSmallIntegerField()
    floor = models.IntegerField()
    services = None  # TODO add - has to be a ForeignKey
    is_valid = models.BooleanField(default=True)


class ResidentialCategory(models.Model):
    title = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Residential(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    # location = models.PointField(geography=True, spatial_index=True)  # TODO import
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city_or_section = models.CharField(max_length=100)
    capacity = models.IntegerField()
    services = None  # TODO add - has to be a ForeignKey
    is_valid = models.BooleanField(default=True)


class HotelComment(AbstractComment):
    comment = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='hotel_comments')


class HotelRoomComment(AbstractComment):
    comment = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='hotel_room_comments')


class ResidentialComment(AbstractComment):
    comment = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='residential_comments')
