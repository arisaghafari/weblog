from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name = "home"),
    path('page/<int:page>', ArticleList.as_view(), name = "home"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name = "detailArticle"),
    path('category/<slug:slug>', CategoryList.as_view(), name = "categoryArticle"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name = "categoryArticle")
]