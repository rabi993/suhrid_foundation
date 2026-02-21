from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination

class PostPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

    
class NoticeViewset(viewsets.ModelViewSet):
    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = PostPagination
    search_fields = ['name', 'description']




from rest_framework.response import Response

class noticeCommentViewset(viewsets.ModelViewSet):
    queryset = models.noticeComment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        
        queryset = super().get_queryset()
        commentor_id = self.request.query_params.get('commentor_id')
        post_id = self.request.query_params.get('notice_id')

        if commentor_id:
            queryset = queryset.filter(commentor_id=commentor_id)
        if post_id:
            queryset = queryset.filter(post_id=post_id)

        return queryset
    
