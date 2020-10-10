from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    path('', home, name = "home"),
    path('page/<int:page>', home, name = "home"),
    path('article/<slug:slug>', detailArticle, name = "detailArticle"),
    path('category/<slug:slug>', categoryArticle, name = "categoryArticle")
]