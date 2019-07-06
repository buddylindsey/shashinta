from os import listdir, path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from images.models import Image


class Command(BaseCommand):
    help = "Import images from MEDIA_ROOT/images"

    def handle(self, *args, **options):
        location = "{}/images".format(settings.MEDIA_ROOT)
        images = [f for f in listdir(location)]

        for image in images:
            if path.isfile("{}/{}".format(location, image)):
                try:
                    Image.objects.create(image="images/{}".format(image))
                except IntegrityError:
                    print("{} is already in the system.".format(image))
