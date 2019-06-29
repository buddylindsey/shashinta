from os import listdir, path

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from django.conf import settings
from images.models import Image


class Command(BaseCommand):
    help = "Import images from MEDIA_ROOT/images"

    def handle(self, *args, **options):
        location = f"{settings.MEDIA_ROOT}/images"
        images = [f for f in listdir(location)]

        for image in images:
            if path.isfile(f"{location}/{image}"):
                try:
                    Image.objects.create(image=f"images/{image}")
                except IntegrityError:
                    print(f"{image} is already in the system.")
