from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# from rest_framework.permissions import BasePermission

# Create your views here.
class PostPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = PostPagination
    search_fields = ['title', 'content', 'category__name']
    # permission_classes = [IsAuthenticatedOrReadOnly]  



from rest_framework.response import Response

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        
        queryset = super().get_queryset()
        commentor_id = self.request.query_params.get('commentor_id')
        post_id = self.request.query_params.get('post_id')

        if commentor_id:
            queryset = queryset.filter(commentor_id=commentor_id)
        if post_id:
            queryset = queryset.filter(post_id=post_id)

        return queryset
    
