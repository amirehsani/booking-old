# Generated by Django 4.1.4 on 2022-12-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_flightticket_price_for_one_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightticket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
