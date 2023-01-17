# Generated by Django 4.1.4 on 2023-01-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='usercart',
            constraint=models.UniqueConstraint(fields=('user', 'cart_number'), name='unique_user_cart'),
        ),
    ]