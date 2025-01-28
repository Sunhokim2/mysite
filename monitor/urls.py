from django.urls import path
from .views import *

urlpatterns = [
    path('status', server_status),  # 서버 상태를 반환하는 API
    path('status2', server_status_api, name='server-status-api'),
    path('dashboard', dashboard, name='dashboard'),
]
