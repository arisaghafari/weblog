from django.shortcuts import render , get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic.list import ListView

"""
def home(request, page=1):
    articleList = Article.objects.published()
    paginator = Paginator(articleList, 3)
    #page = request.GET.get("page")
    articles = paginator.get_page(page)
    context = {
        "articles" : articles
    }
    return render(request, "blog/home.html", context)
"""
class ArticleList(ListView):
    paginate_by = 3
    #context_object_name = "articles"
    template_name = "blog/home.html"
    queryset = Article.objects.published()

def detailArticle(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug = slug)
    }
    return render(request, "blog/detailArticle.html", context)

def categoryArticle(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articlesList = category.article.published()
    paginator = Paginator(articlesList, 3)
    #page = request.GET.get("page")
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "articles": articles
    }
    return render(request,"blog/categoryArticle.html", context)
