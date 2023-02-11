from django.db import models
from django.utils.safestring import mark_safe


class AbstractImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='statics')
    created_time = models.DateTimeField(auto_now_add=True)

    def image_show(self):
        return mark_safe('<img src="/static/%s" width="150" height="150" />' % self.image)

    image_show.short_description = 'image'

    class Meta:
        abstract = True


class ResidentialGallery(models.Model):
    id = models.AutoField(primary_key=True)


class HotelRoomGallery(models.Model):
    id = models.AutoField(primary_key=True)


class AirportGallery(models.Model):
    id = models.AutoField(primary_key=True)


class ResidentialImage(AbstractImage):
    gallery = models.ForeignKey(ResidentialGallery, on_delete=models.DO_NOTHING, null=True, blank=True)


class HotelRoomImage(AbstractImage):
    gallery = models.ForeignKey(HotelRoomGallery, on_delete=models.DO_NOTHING, null=True, blank=True)


class AirportImage(AbstractImage):
    gallery = models.ForeignKey(AirportGallery, on_delete=models.DO_NOTHING, null=True, blank=True)
