from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username = models.CharField(max_length=100, unique=True)
    # name = models.CharField(max_length=100)

    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)

    # USERNAME_FIELD = username
    # REQUIRED_FIELDS = name
