from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,default="Title")
    body = models.CharField(max_length=20000,default="")
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    image = models.ImageField(upload_to='images/', default="")
    link = models.URLField(max_length=250,default="")


class CountryData(models.Model):
    Measle = 'measle'
    Sickness = 'sickness'
    Flue = 'flue'
    Other = 'others'
    DISEASE_CHOICES = [
        (Measle, 'Measle'),
        (Sickness, 'Sickness'),
        (Flue, 'Flue'),
        (Other, 'Others')
    
    ]
    name = models.CharField(max_length=100, default="")
    disease = models.CharField(max_length=100, choices=DISEASE_CHOICES)
    age = models.IntegerField(null=True)




