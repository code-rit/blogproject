from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from .views import ArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view())
]