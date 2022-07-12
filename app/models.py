from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    info = models.TextField()
    image = models.ImageField()