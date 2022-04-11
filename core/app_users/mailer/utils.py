import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..short_token.utils import ShortToken
from ..redis_key.utils import CreateRedisKey


class Mailer:
    @staticmethod
    def send_mail(email, user_id) -> bool:
        token = ShortToken.create_short_token()
        sender = 'Подтверждение почты от Тестового сайта'
        subject = 'Подтверждение почты'
        text = 'Для подтверждения почты перейдите по ссылке: http://127.0.0.1'\
               f':8000/users/activate/{token}'

        redis_token = CreateRedisKey()
        redis_token.create_redis_key(token, user_id)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        try:
            server.login(os.getenv("site_email"), os.getenv("email_password"))
            server.sendmail(
                os.getenv("site_email"),
                email,
                msg.as_string()
            )
            server.quit()

            return True
        except Exception:
            return False


"""
    Подтверждение почты
    Подтверждение почты от Тестового сайта Сегодня, 13:55
    Для подтверждения почты перейдите по ссылке: 
    http://127.0.0.1:8000/user/activate/GFfw344
"""
