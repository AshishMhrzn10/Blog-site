from django.shortcuts import render
from .models import *
from marketing.models import Signup

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup(email=email)
        new_signup.save()

    context={
        'featured_post':featured,
        'latest_post':latest
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})