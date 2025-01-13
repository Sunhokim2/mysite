from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        return render(request, "mysite/main.html")

    def post(self,request):
        print("포스트 호출")
        return render(request, "mysite/main.html")
