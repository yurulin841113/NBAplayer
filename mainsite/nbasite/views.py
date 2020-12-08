from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import datetime


# Create your views here.
# def homepage(request):
#     posts = Post.objects.all()
#     post_list = list()
#
#     for i, post in enumerate(posts):
#         post_list.append(f"No.{i}\t{post.title}<br><hr>")
#         post_list.append(f"<small>{post.body}</small><br><br>")
#
#     return HttpResponse(post_list)

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', {
        'post_list': posts, 'current_time': now,
    })


def showpost(request, pk):
    post = Post.objects.get(pk=pk)
    if post is not None:
        return render(request, 'post.html', {
            'post_detail': post, 
        })
