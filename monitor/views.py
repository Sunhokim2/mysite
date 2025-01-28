import datetime

import psutil
from django.http import JsonResponse
from django.shortcuts import render

from .models import ServerStatus


def server_status(request):
    # # 서버 상태 데이터 수집
    # data = {
    #     "cpu_usage": psutil.cpu_percent(),
    #     "memory_usage": psutil.virtual_memory().percent,
    #     "disk_usage": psutil.disk_usage('/').percent
    # }

    # 서버 상태 수집
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # 데이터 저장
    ServerStatus.objects.create(cpu_usage=cpu, memory_usage=memory, disk_usage=disk)
    print(f"Collected at {datetime.now()}: CPU={cpu}%, Memory={memory}%, Disk={disk}%")

def server_status_api(request):
    # 최근 10개의 서버 상태 데이터 반환
    data = ServerStatus.objects.order_by('-timestamp')[:10]
    response = {
        "timestamps": [status.timestamp.strftime('%Y-%m-%d %H:%M:%S') for status in data],
        "cpu_usages": [status.cpu_usage for status in data],
        "memory_usages": [status.memory_usage for status in data],
        "disk_usages": [status.disk_usage for status in data],
    }
    return JsonResponse(response)

def dashboard(request):
    return render(request, 'monitor/dashboard.html')