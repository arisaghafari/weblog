from django.urls import path
from .views import home, detailArticle

app_name = "blog"
urlpatterns = [
    path('', home, name = "home"),
    path('article/<slug:slug>', detailArticle, name = "detailArticle")
]