from djongo import models


class Customer(models.Model):
    username = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    
    def __str__(self) -> str:
        return self.username
