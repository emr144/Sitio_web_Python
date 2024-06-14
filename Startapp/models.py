# en Startapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField( upload_to='profile_images', blank=True, null=True)

    def __str__(self):
        return f'{self.username} Profile'
