
from django.urls import path
from .views import (
  youtube_videos,
)

app_name = "youtube"
urlpatterns = [
    path('', youtube_videos, name='youtube_videos'),
]
