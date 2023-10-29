from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

route = DefaultRouter(trailing_slash=False)

route.register(r'article/', ArticleViewSet, basename = 'article')
urlpatterns = [
    re_path(r"^", include(route.urls))
]
