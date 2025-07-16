from django.db import models

# Create your models here.
class UserDetails(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    agent = models.BooleanField()
    username = models.CharField()