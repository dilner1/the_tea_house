from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=odels.CASCADE)
    f_name = models.CharField(max_length=30, null=True)
    l_name = models.CharField(max_length=30, null=True)
    email = models.EmailField()