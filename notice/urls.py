from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.NoticeViewset) 
router.register('comments', views.noticeCommentViewset) 
urlpatterns = [
    path('', include(router.urls)),
]


