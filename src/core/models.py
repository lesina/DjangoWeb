from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    email = models.EmailField(('email address'), blank=False, unique=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:user', kwargs={'slug': self.username})

    def get_pubs(self):
        return self.videos

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'