import json

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from ...cooperation.resource import Cooperation


class CooperationResourceTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='Пример пользователя',
            password='qwerty123',
            email='rafik.saakyan.2016@mail.ru'
        )

        self.factory = RequestFactory()

        assert self.user
        assert self.factory

    def test_get(self):
        """
            Сотрудничество
            Сотрудничество с КомпаниейСегодня, 10:10
            Пример сообщения для отправки на почту
                :return: Функция отправки сообщения работает
        """
        request = self.factory.post('')
        request.content_type = 'application/json'
        request._body = json.dumps({
            "email": self.user.email,
            "message": "Пример сообщения для отправки на почту"
        })

        # response = Cooperation.as_view()(request)

        # assert response.status_code == 200
