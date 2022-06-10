from django.shortcuts import render
from . models import Post

# Create your views here.


def index(request):
    
    posts = Post.objects.all()
    context = {"post":posts}
    return render(request, 'index.html', context)