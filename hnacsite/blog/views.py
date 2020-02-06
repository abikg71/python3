from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

# Create your views here.
#Dummi Data
posts = [
    {
        'author': 'Abinet Kenore ',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Feb 03, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 03, 2020'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

    #return HttpResponse('<h1> Blog Home </h1>')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

    #return HttpResponse('<h1> Blog About </h1>')
def profile(request):
    return render(request, 'blog/profile.html')
