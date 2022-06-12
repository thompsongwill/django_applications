from importlib.resources import path
from unicodedata import name
from django.urls import path
from .import views





urlpatterns = [
    path('', views.home, name='home'),
]