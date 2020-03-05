from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mayur',
        'title': 'sometitle',
        'content': 'some random text',
        'date_posted': 'just now',

    }
]



def home(request):
    context = {
            'posts': posts
                }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
