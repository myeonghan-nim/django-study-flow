from django.shortcuts import render

from .models import Post


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    post = Post()
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.save()
    return render(request, 'create.html')
