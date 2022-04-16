from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver 
from django.db.models.signals import post_save

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


