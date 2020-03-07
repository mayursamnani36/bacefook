from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


@login_required()
def about(request):
    return render(request, 'blog/about.html')
