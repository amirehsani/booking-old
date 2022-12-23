# Generated by Django 4.1.4 on 2022-12-23 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('air', '0001_initial'),
        ('comment', '0001_initial'),
        ('residence', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='residentialcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='residentialcomment',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotelroomcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room_comments', to='residence.hotelroom'),
        ),
        migrations.AddField(
            model_name='hotelroomcomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.hotelroomcomment'),
        ),
        migrations.AddField(
            model_name='hotelroomcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotelroomcomment',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotelcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_comments', to='residence.hotel'),
        ),
        migrations.AddField(
            model_name='hotelcomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.hotelcomment'),
        ),
        migrations.AddField(
            model_name='hotelcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotelcomment',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airportcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_comments', to='air.airport'),
        ),
        migrations.AddField(
            model_name='airportcomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.airportcomment'),
        ),
        migrations.AddField(
            model_name='airportcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airportcomment',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airlinecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_comments', to='air.airline'),
        ),
        migrations.AddField(
            model_name='airlinecomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.airlinecomment'),
        ),
        migrations.AddField(
            model_name='airlinecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airlinecomment',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
    ]
