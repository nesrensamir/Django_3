from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movies
from django.core.mail import send_mail


@receiver(post_save, sender=Movies)
def my_handler(sender, instance, created, *args, **kwargs):
      send_mail('create new movie', 'Dear user {} has been created'.format(instance.name),
      'nesrinsamir@gmail.com', ['receiver-1', 'receiver-2'], fail_silently=False)