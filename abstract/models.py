from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from core import settings


class AbstractRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_%(class)ss')
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40

    COMMENT_STATUS_CHOICES = (
        (CREATED, 'Created'), (APPROVED, 'Approved'), (REJECTED, 'Rejected'), (DELETED, 'Deleted')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)s')
    # 'validated_by' shows who accepted the comment to be published
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=COMMENT_STATUS_CHOICES, default=CREATED)

    class Meta:
        abstract = True


class AbstractHotelOrHotelRoomFeature(models.Model):
    title = models.CharField(max_length=80)
    is_active = models.BooleanField(default=False)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractHotelOrResidential(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city_or_section = models.CharField(max_length=100, verbose_name='City or Section')
    address = models.TextField()
    map_link = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(unique=True, validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')])

    number_of_rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                          verbose_name='Number of Rooms')
    floors = models.PositiveSmallIntegerField()
    capacity = models.IntegerField()
    area = models.IntegerField()

    is_valid = models.BooleanField(default=True)

    class Meta:
        abstract = True
