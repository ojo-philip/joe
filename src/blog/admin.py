from django.contrib import admin
from .models import Tags, Post

admin.site.site_header = "Jesus Over Everything"

class PostAdmin(admin.ModelAdmin):

  list_display = ["title", 'timestamp', 'status']
  list_filter = ["title", 'timestamp', 'content', 'status']


# Register your models here.
admin.site.register(Tags)
admin.site.register(Post, PostAdmin)
