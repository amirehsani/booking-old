# Generated by Django 4.1.5 on 2023-02-11 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0005_rename_hotel_hotelroom__hotel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelroom',
            old_name='_hotel',
            new_name='hotel',
        ),
        migrations.RenameField(
            model_name='hotelroom',
            old_name='_id',
            new_name='id',
        ),
    ]