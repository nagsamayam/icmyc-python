from django.db import models
from django.db.models import signals
from .utils import unique_slug_generator
from django.urls import reverse


class Complaint(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('complaint-detail', kwargs={'slug': self.slug})


def complaint_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.title = instance.title.capitalize()
    instance.body = instance.body.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


signals.pre_save.connect(complaint_pre_save_receiver, sender=Complaint)
