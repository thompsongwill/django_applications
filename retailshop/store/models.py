from email.mime import image
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/images")
    des = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.title