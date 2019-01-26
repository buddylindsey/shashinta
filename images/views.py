from os import listdir
from os.path import isfile, join

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ImageUploadForm


class ListImagesView(TemplateView):
    template_name = "images/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = [f for f in listdir(join(settings.BASE_DIR, settings.MEDIA_ROOT))]
        context["images"] = images
        return context


class UploadImageView(FormView):
    form_class = ImageUploadForm
    template_name = "images/upload.html"
    success_url = reverse_lazy("list_images")

    def form_valid(self, form):
        image = self.request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(image.name, image)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
