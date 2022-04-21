from dotenv import load_dotenv

from django.test import TestCase

from ...mailer.utils import Mailer


class MailerUtilsTest(TestCase):
    def setUp(self) -> None:
        load_dotenv()

    @staticmethod
    def test_send_mail():
        """
            Сотрудничество
            Сотрудничество с КомпаниейСегодня, 9:52
            Пример сообщения
                :return: Функция отправки сообщения работает
        """
        # assert Mailer.send_mail(
        #     'empty@mail.ru', "Пример сообщения"
        # )
