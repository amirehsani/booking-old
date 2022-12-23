from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    phone_number = models.PositiveBigIntegerField(unique=True, null=True, blank=True, validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')])

    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)

    # USERNAME_FIELD = username
    # REQUIRED_FIELDS = name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=60, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    nationality = models.CharField(max_length=64, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# class UserManager(models.Model):
