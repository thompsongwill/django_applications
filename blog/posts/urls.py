from django.urls import path
from . import views

app_name = 'posts'



urlpatterns = [
    path('', views.index, name='home'),
    path('<str:blog_id>/', views.single_post, name='post'),
]