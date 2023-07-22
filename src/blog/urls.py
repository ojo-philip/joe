
from django.urls import path
from .views import (
  home,
  blog_page,
  post_detail,
  about_page,
  # contact_page,
  tags_page
)

app_name = "blog"
urlpatterns = [
    path('', home, name='home_page'),
    path('blog/', blog_page, name='blog_page'),
    path('about/', about_page, name='about_page'),
    # path('contact-us/', contact_page, name='contact_page'),
    path('<int:pk>/<str:slug>/', post_detail, name='post_detail'),
    path('tag/<int:pk>/<str:slug>/', tags_page, name='tags_page'),

]
