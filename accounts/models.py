from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
