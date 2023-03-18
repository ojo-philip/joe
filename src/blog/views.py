from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from urllib.parse import quote_plus
from .pagination import pagination


def about_page(request):
  
  return render(request, "blog/about.html")

def contact_page(request):
  
  return render(request, "blog/contact.html")


def home(request):
  latest_posts = Post.objects.filter(status='Published')[: 6]
  context = {
    "latest_posts": latest_posts,
  }
  return render(request, "blog/index.html", context)


def blog_page(request):
  blog_posts = Post.objects.filter(status="Published")

  pages = pagination(request, blog_posts, 12)
  context = {
    # "blog_posts": blog_posts,
    'items': pages[0],
    'page_range': pages[1],
  }
  return render(request, "blog/article.html", context)


def post_detail(request, slug, pk):
  post_detail = get_object_or_404(Post, slug=slug, pk=pk)
  share_shring = quote_plus(post_detail.content)
  recent_posts = Post.objects.filter(status="Published")[:3]
  context = {
    "post_detail": post_detail,
    "recent_posts": recent_posts,
    "share_shring": share_shring,
  }
  return render(request, "blog/post.html", context)


def tags_page(request, slug, pk):
    post = Post.objects.filter(status='Published').order_by('-id')
    if slug and pk:
        tag = get_object_or_404(Tags, slug=slug, pk=pk)
        post = post.filter(tags=tag)
        pages = pagination(request, post, 12)
    context = {
        'tag': tag,
        'post': post,
        'items': pages[0],
        'page_range': pages[1]
    }
    return render(request, 'blog/tags.html', context)