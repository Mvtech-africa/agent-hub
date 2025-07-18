from django.db import models
from user.models import UserDetails

class Property(models.Model):
    agent = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='apartment')
    title = models.CharField(max_length=200)
    description = models.TextField()
    apartment_type = models.CharField(max_length=100, choices=[
        ('studio', 'Studio'),
        ('1_bedroom', '1 Bedroom'),
        ('2_bedroom', '2 Bedroom'),
        ('3_bedroom', '3 Bedroom'),
        ('4_bedroom', '4 Bedroom'),
        ('5_bedroom', '5 Bedroom'),
        ('duplex', 'Duplex'),
        ('penthouse', 'Penthouse'),
        ('villa', 'Villa'),
        ('townhouse', 'Townhouse'),
        ('condo', 'Condo'),
        ('cottage', 'Cottage'),
        ('bungalow', 'Bungalow'),
        ('loft', 'Loft'),
        ('other', 'Other')
    ])
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image1 = models.ImageField(upload_to='image/')
    image2 = models.ImageField(upload_to='image/')
    image3 = models.ImageField(upload_to='image/')
    video_file = models.FileField(upload_to='property_videos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField('text_duration in seconds')
    property_address = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.title} by {self.agent.username}' 

