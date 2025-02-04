#쟝고 튜토리얼을 위한 코드입니다. 변경될 수 있어요

25.01.14 : 클론코딩 종료\n

|앞으로는 배포를 해볼 예정

25.01.22 : 배포 완료.

http://clonestar.duckdns.org/main

📌 프로젝트 개요

DjangoMovie는 Django 프레임워크를 기반으로 한 웹 애플리케이션으로, 영화 관련 정보를 관리하고 제공하는 기능을 포함하고 있습니다.

🚀 설치 방법

1️⃣ 저장소 클론

```
git clone <repository_url>
cd DjangoMovie
```

2️⃣ 가상 환경 생성 및 활성화

```
python -m venv venv
source venv/bin/activate #가상환경 접속
```

3️⃣ 필수 패키지 설치

```
pip install -r requirements.txt
```

4️⃣ 데이터베이스 마이그레이션

```
python manage.py makemigrations
python manage.py migrate
```

5️⃣ 서버 실행 ( AWS가 아닌 파이썬 장고 자체 실행의 경우 )

```
python manage.py runserver
```
