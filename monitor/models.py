from django.db import models

class ServerStatus(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # 수집 시간
    cpu_usage = models.FloatField()                     # CPU 사용률
    memory_usage = models.FloatField()                  # 메모리 사용률
    disk_usage = models.FloatField()                    # 디스크 사용률

    def __str__(self):
        return f"CPU: {self.cpu_usage}%, Memory: {self.memory_usage}%, Disk: {self.disk_usage}% at {self.timestamp}"
