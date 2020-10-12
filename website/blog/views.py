from django.shortcuts import render , get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

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
    #template_name = "blog/home.html"
    queryset = Article.objects.published()

"""
def detailArticle(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug = slug)
    }
    return render(request, "blog/detailArticle.html", context)
"""
class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug = slug)

"""
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
"""
class CategoryList(ListView):
    template_name = "blog/category_list.html"
    paginate_by = 3

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug, status=True)
        return category.article.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
