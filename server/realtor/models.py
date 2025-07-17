from django.db import models
from user.models import UserDetails

class Property(models.Model):
    agent = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title

