from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email =models.CharField(max_length=40)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username