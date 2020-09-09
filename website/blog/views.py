from django.shortcuts import render
from .models import Article

def home(request):
    context = {
        "articles" : Article.objects.filter(status="p").order_by("-publish")[:5]
    }
    return render(request, "blog/home.html", context)

def detailArticle(request, slug):
    context = {
        "article" : Article.objects.get(slug = slug)
    }
    return render(request, "blog/detailArticle.html", context)
