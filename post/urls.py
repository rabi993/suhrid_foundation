from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.PostViewset) 
router.register('comments', views.CommentViewset) 

urlpatterns = [
    path('', include(router.urls)),
]