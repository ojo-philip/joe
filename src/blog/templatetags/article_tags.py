from django import template
from blog.models import Post, Tags

register = template.Library()




@register.inclusion_tag("blog/navtag.html")
def navtag_tags():
    tags = Tags.objects.order_by('title')
    return {
        "tags": tags,
    }
