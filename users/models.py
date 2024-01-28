from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .managers import ProcsUserManager

# Create your models here.

class ProcsUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=11, blank=True)
    image = models.ImageField(upload_to="profile-images")
    birthday = models.DateField(null=True, blank=True)
    isProcsAdmin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ProcsUserManager()

    def __str__(self):
        return self.email
