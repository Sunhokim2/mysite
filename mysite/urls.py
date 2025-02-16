"""
URL configuration for mysite project.

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
from django.urls import include,path

from .views import Sub
from content.views import Main, UploadFeed
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('what/',Sub.as_view()),
    path('polls/', include('polls.urls')),
    path("admin/", admin.site.urls),

    path('main/',Main.as_view()),
    path('content/',include('content.urls')),
    path('user/',include('user.urls')),
    
    # 서버상태 모니터링 API
    path('monitor/', include('monitor.urls')),  # monitor API 추가
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
