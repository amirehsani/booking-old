from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)


class Airplane(models.Model):
    manufacturer = models.CharField(max_length=60)
    name = models.CharField(max_length=50)
    register_number = models.BigIntegerField()
    number_of_seats = models.IntegerField()


class Airport(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
