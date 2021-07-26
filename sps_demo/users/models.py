from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
