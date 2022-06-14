from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm

# Create your views here.


def home(request):
    return render(request, 'todo/home.html', {})

 
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',{"form":UserCreationForm(), 'error':'User name already'})
        else:
            return render(request, 'todo/signupuser.html',{"form":UserCreationForm(), 'error':'Passwords did not match'})
        
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'todo/signin.html', {'form':AuthenticationForm()})
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
           return render(request, 'todo/signin.html', {'form':AuthenticationForm(), 'error':'Username or Password did not match'})
       else:
           login(request,user)
           return redirect('tasks')
       
       
def tasks(request):
    return render(request, 'todo/tasks.html')


def newTask(request):
    if request.method == "GET":
        return render(request, 'todo/todo.html', {'form':TodoForm()})
    
    else:
        form = TodoForm(request.POST)
        new_to_do = form.save(commit=False)
        new_to_do.user = request.user
        new_to_do.save()


