from django.urls import path
from . import views


urlpatterns = [ 
               path('', views.home, name='home'),
                path('signup/', views.signupuser, name='signup'),
                path('todos/', views.tasks, name='tasks'),
                path('login/', views.signin, name='signin'),
                path('logout/', views.signout, name='signout'),
                path('create/', views.newTask, name='todo'),
               ]