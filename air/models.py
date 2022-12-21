from django.db import models
from comment.models import AbstractComment


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
    country = None
    city = None


class AirlineComment(AbstractComment):
    comment = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airline_comments')


class AirportComment(AbstractComment):
    comment = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airport_comments')
