from email.mime import image
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/images")
    des = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.title