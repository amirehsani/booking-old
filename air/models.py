from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100, verbose_name='Origin Country')


class Airplane(models.Model):
    manufacturer = models.CharField(max_length=60)
    name = models.CharField(max_length=50)
    register_number = models.BigIntegerField(verbose_name='Register Number')
    number_of_seats = models.IntegerField(verbose_name='Number of Seats')


class Airport(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
