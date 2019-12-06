from django.shortcuts import render


posts = [
    {
        'author': "coreyMS",
        'title': 'blog post 1',
        'content': "First post content",
        'date-posted': "august 24, 2018"
    },
    {
        'author': "harhsit",
        'title': 'blog post 2',
        'content': "First2 post content",
        'date-posted': "august 28, 2018"
    },
    {
        'author': "arpit",
        'title': 'blog post 1',
        'content': "First post content",
        'date-posted': "august 24, 2018"
    }

]

# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
