from django.shortcuts import render , get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator

def home(request, page=1):
    articleList = Article.objects.published()
    paginator = Paginator(articleList, 3)
    #page = request.GET.get("page")
    articles = paginator.get_page(page)
    context = {
        "articles" : articles
    }
    return render(request, "blog/home.html", context)

def detailArticle(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug = slug)
    }
    return render(request, "blog/detailArticle.html", context)

def categoryArticle(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request,"blog/categoryArticle.html", context)
