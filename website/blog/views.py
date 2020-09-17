from django.shortcuts import render , get_object_or_404
from .models import Article, Category

def home(request):
    context = {
        "articles" : Article.objects.filter(status="p"),
        "categoris" : Category.objects.filter(status=True)
    }
    return render(request, "blog/home.html", context)

def detailArticle(request, slug):
    context = {
        "article" : get_object_or_404(Article, slug = slug, status="p"),
        "categoris": Category.objects.filter(status=True)
    }
    return render(request, "blog/detailArticle.html", context)
