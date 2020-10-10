from django import template
from ..models import Category
register = template.Library()

@register.simple_tag()
def title(data = "وبلاگ جنگویی من"):
    return data

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "categoris": Category.objects.filter(status=True)
    }
