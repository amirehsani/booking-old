# Generated by Django 4.1.4 on 2022-12-22 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residence', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentialRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='residence.residential')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hotel_room_rate', to='residence.hotelroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
