from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class BannerViewset(viewsets.ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer

