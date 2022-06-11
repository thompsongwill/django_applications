from django.shortcuts import render, get_list_or_404
from . models import Post

# Create your views here.


def index(request):
    
    posts = Post.objects.all()
    context = {"post":posts}
    return render(request, 'index.html', context)


def single_post(request, blog_id):
    blog = get_list_or_404(Post, pk=blog_id)
    detail =  {"posts":blog}
    return render(request, 'posts.html',detail)