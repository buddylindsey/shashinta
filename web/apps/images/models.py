from django.db import models

from django_extensions.db.models import TimeStampedModel

from core.models.fields import FileChecksumField
from django.urls import reverse


class Image(TimeStampedModel):
    image = models.ImageField(upload_to="images")
    file_hash = FileChecksumField(field="image", max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.image.name

    def get_absolute_url(self):
        return reverse("image", args=[self.pk])
