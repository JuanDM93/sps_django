from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
