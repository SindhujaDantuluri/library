from django.contrib.auth.models import User
from django.db import models



class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default=True)
    