"""
URL configuration for suhrid_foundation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . views import UserViewSet, send_email
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('contact_us/', include('contact_us.urls')),
    # path('service/', include('service.urls')),
    path('gift/', include('gift.urls')),
    path('department/', include('department.urls')),
    path('complaint/', include('complaint.urls')),
    path('application/', include('application.urls')),
    path('account/', include('account.urls')),
    path('banner/', include('banner.urls')),
    path('societyApplication/', include('societyApplication.urls')),
    # path('blood/', include('blood.urls')),
    # path('category/', include('category.urls')),
    path('transaction/', include('transaction.urls')),
    path('people/', include('people.urls')),
    path('post/', include('post.urls')),
    path('notice/', include('notice.urls')),
    path('event/', include('event.urls')),
    # path('message/', include('message.urls')),
    path('send-email/', send_email, name='send_email'),
    path('payment/', include('payment.urls')),
    # path('newsletter/', include('newsletter.urls')),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)