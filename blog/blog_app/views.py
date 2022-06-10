from django.shortcuts import render

# Create your views here.

def home(request):
    context = {"greetings": "Hello World"}
    return render(request, 'base.html', context)