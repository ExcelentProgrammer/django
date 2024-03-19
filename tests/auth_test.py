from django.template.defaulttags import url
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from core.apps.api.v1.auth.views import RegisterView
from core.http.database.factory import UserFactory


class RegisterViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RegisterView.as_view()

    def test_register_user(self):
        data = {
            'phone': '+998901234567',
            "jshir": "1",
            'password': 'password'
        }
        request = self.factory.post(url("register"), data=data)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'You have successfully registered.')

    def test_register_user_with_invalid_phone(self):
        data = {
            'phone': 'invalid_phone',
            "jshir": "1",
            'password': 'password'
        }
        request = self.factory.post(url("register"), data=data)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid phone number.')

    def test_register_user_with_invalid_confirmation_code(self):
        user = UserFactory()
        data = {
            'phone': user.handle()['phone'],
            'code': 'invalid_code'
        }
        request = self.factory.post(url("register"), data=data)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid confirmation code.')
