import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password

from mysite.settings import MEDIA_ROOT
from mysite.settings import MEDIA_URL

class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html",{"media_url": MEDIA_URL})

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.png")

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            # json타입인거 설정하고 리턴
            return Response(status=400, data=dict(message="email이 잘못되었습니다."), content_type="application/json")

        if user.check_password(password): # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email
            request.session['nickname'] = user.nickname
            request.session.set_expiry(3600)  # 세션 유지 시간 설정 (1시간)

            return Response(status=200, data=dict(message=f"로그인 성공. {user.nickname}님 환영합니다."), content_type="application/json")
        else:
            return Response(status=400, data=dict(message="비밀번호가 잘못되었습니다."), content_type="application/json")


class LogOut(APIView):
    def get(self, request):
        session_data = request.session.items()

        request.session.flush()
        return render(request, "user/login.html",{'session_data':session_data})


class UploadProfile(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()

        return Response(status=200)