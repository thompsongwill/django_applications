from distutils.command.upload import upload
from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=500, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="media/images")
    created = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title