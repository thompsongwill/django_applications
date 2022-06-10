from distutils.command.upload import upload
from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    tile = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to="media/images")
    created = models.DateTimeField(default=datetime.now, blank=True)