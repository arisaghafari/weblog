from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name = "home"),
    path('page/<int:page>', ArticleList.as_view(), name = "home"),
    path('article/<slug:slug>', detailArticle, name = "detailArticle"),
    path('category/<slug:slug>', categoryArticle, name = "categoryArticle"),
    path('category/<slug:slug>/page/<int:page>', categoryArticle, name = "categoryArticle")
]