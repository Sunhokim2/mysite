from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse
from .models import User

class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email="test_login@naver.com",
            nickname="test_nickname",
            name="test_name",
            password=make_password("test_password"),
            profile_image="default_profile.png"
        )

    def test(self):
        self.assertEqual(1,1)

    def test_join(self):
        response = self.client.post('/user/join', {'email': 'test_email@naver.com',
                                                    'nickname': 'test_nickname',
                                                    'name': 'test_name',
                                                    'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '회원가입')

        user = User.objects.filter(email="test_email@naver.com").first()

        self.assertEqual(user.nickname, 'test_nickname')
        self.assertEqual(user.name, 'test_name')
        self.assertTrue(user.check_password, 'test_password')
    def test_login(self):
        response = self.client.post('/user/login', {
            'email': 'test_login@naver.com',
                                                    'password': 'test_password'})
        self.assertEqual(response.status_code, 200)