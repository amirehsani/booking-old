from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from abstract.models import AbstractRate, AbstractHotelOrResidential, AbstractHotelOrHotelRoomFeature


class ResidentialCategory(models.Model):
    title = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Hotel(AbstractHotelOrResidential):
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_of_hotel_room')
    room_number = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()

    capacity = models.IntegerField()
    single_beds = models.PositiveSmallIntegerField()
    double_beds = models.PositiveSmallIntegerField()
    extra_beds = models.PositiveSmallIntegerField()

    rate = models.ForeignKey(AbstractRate, on_delete=models.DO_NOTHING, related_name='hotel_room_rate')

    is_valid = models.BooleanField(default=True)


class Residential(AbstractHotelOrResidential):
    residential_category = models.ForeignKey(ResidentialCategory, on_delete=models.DO_NOTHING)
    rate = models.ForeignKey(AbstractRate, on_delete=models.DO_NOTHING)


class HotelRoomFeature(AbstractHotelOrHotelRoomFeature):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_feature')
