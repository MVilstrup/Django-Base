# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as locale
from django.dispatch import receiver
from django.db.models.signals import post_save

from . import managers

# Create your models here.

class Profile(models.Model):
    #Relations
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            related_name="profile",
            verbose_name=locale("user")
            )

    #Attributes 
    interactions = models.PositiveIntegerField(
                    default=0,
                    verbose_name=locale("interactions")
                    )

    #Object
    objects = managers.ProfileManager()

    #Custom Property
    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    # Methods


    # Meta & String
    class Meta:
        verbose_name = locale("profile")
        verbose_name_plural = locale("profiles")
        ordering = ("user", )

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()
