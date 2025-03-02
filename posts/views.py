from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
def posts_list(request):
    posts = models.Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post(request, slug):
    post = models.Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{'post': post})

@login_required(login_url="/users/login")
def create_post(request):
    return render(request, 'posts/post_new.html')