from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArticleFilter

    
