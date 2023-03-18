from django.shortcuts import render
from .models import Video
from blog.pagination import pagination

# Create your views here.

def youtube_videos(request):
  videos = Video.objects.all()
  pages = pagination(request, videos, 12)
  context = {
    'items': pages[0],
    'page_range': pages[1],
  }
  return render(request, "youtube/worship.html", context)