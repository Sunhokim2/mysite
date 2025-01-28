from django.urls import path
from .views import server_status

urlpatterns = [
    path('status', server_status),  # 서버 상태를 반환하는 API
]
