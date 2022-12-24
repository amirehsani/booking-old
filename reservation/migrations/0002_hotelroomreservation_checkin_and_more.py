# Generated by Django 4.1.4 on 2022-12-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroomreservation',
            name='checkin',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hotelroomreservation',
            name='checkout',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hotelroomreservation',
            name='count_of_nights',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='residentialreservation',
            name='checkin',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='residentialreservation',
            name='checkout',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='residentialreservation',
            name='count_of_nights',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='flightticketreservation',
            name='number_of_passengers',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
