import hashlib

from django.db import models


class FileChecksumField(models.CharField):
    description = "Create sha checksum of an uploaded file"

    def __init__(self, *args, field=None, **kwargs):
        self._field = field
        super().__init__(*args, **kwargs)

    def update_field(self, model_instance):
        sha = hashlib.sha3_256()
        upload = getattr(model_instance, self._field)
        for chunk in upload.chunks():
            sha.update(chunk)
        return sha.hexdigest()

    def pre_save(self, model_instance, add):
        if add:
            value = self.update_field(model_instance)
            setattr(model_instance, self.attname, value)
            return value
        return super().pre_save(model_instance, add)
