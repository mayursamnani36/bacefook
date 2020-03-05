from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mayur',
        'content': 'some random text',
        'created_at': 'just now',

    }
]



def home(request):
    context = {
            'posts': posts
                }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
