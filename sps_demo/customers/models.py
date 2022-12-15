from djongo import models
from accounts.models import Account


class Customer(models.Model):
    _id = models.ObjectIdField(default=0)
    username = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    accounts = models.ArrayField(
        model_container=Account, default=None
    )

    def __str__(self) -> str:
        return self.username
