from . import serializers
from . import models
from rest_framework import viewsets
from . import models, serializers
from rest_framework import filters, pagination

# Create your views here.
class BlogPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    max_page_size = 100

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','topic','title']