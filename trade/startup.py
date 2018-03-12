import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from . import utils
from .models import Item


@receiver(post_save, sender=Item, dispatch_uid="rotate_item_image")
def update_image(sender, instance, **kwargs):
    if instance.photo:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.photo.url
        utils.rotate_image(fullpath)
