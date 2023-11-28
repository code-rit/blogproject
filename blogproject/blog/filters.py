from django.db.models import Q
import django_filters
from blog.models import Article

class ArticleFilter(django_filters.FilterSet):
    # Define filter fields based on your requirements
    heading = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.NumberFilter(field_name='categories__id')


    class Meta:
        model = Article
        fields = ['heading', 'content', 'category']
