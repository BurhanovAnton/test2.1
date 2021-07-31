from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    avatar = models.ImageField(upload_to='users/')
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)


