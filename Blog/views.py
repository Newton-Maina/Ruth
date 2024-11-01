from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import Post

# Create your views here.

# def index(request):
#     return HttpResponse('Hi there This is a Blog App for Ruth')

def post_list(request):
    posts = Post.objects.filter(status=1).order_by('created_at')
    return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'post_detail.html', {'post':post})