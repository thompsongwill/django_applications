from distutils.command.upload import upload
from email.policy import default
import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pictures')
    contact_number = models.CharField(max_length=100, default='08111xxx999')
    gender = models.CharField(max_length=8, default=False)
    business = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.user.username