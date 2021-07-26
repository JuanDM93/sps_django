from djongo import models


class Account(models.Model):
    _id = models.ObjectIdField(default=0)
    account_id = models.IntegerField(unique=True)
    limit = models.IntegerField()
