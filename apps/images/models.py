from django.db import models

from django_extensions.db.models import TimeStampedModel

from core.models.fields import FileChecksumField


class Image(TimeStampedModel):
    image = models.ImageField(upload_to="images")
    file_hash = FileChecksumField(field="image", max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.image.name
