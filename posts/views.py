from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        new_post = Post(title=title, body=body)
        new_post.save()
        return redirect('index')
    else:
        return render(request, 'addblog.html')
def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})