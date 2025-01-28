import psutil
from django.http import JsonResponse

def server_status(request):
    # 서버 상태 데이터 수집
    data = {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }
    return JsonResponse(data)
