from django.shortcuts import render
from . models import Blog
# Create your views here.

def myblog(request):
    post=Blog.objects.all()
    return render(request,'blog/myblog.html', {'post': post})