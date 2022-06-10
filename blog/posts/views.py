from django.shortcuts import render
from . models import Post

# Create your views here.


def index(request):
    
    posts = Post.objects.all()
    context = {"post":posts}
    return render(request, 'index.html', context)


def single_post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'posts':post}
    return render(request, 'post.html', context)