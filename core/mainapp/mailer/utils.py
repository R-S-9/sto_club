import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    @staticmethod
    def send_mail(email: str, message: str) -> bool:
        sender = "Сотрудничество с Компанией"
        subject = "Сотрудничество"

        try:
            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = sender
            msg["Reply-To"] = sender
            msg["Reply-Path"] = sender
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login(os.getenv('admin_mail'), os.getenv('admin_password'))
            server.sendmail(
                os.getenv('admin_mail'),
                email,
                msg.as_string()
            )
            server.quit()

            return True
        except Exception as _ex:
            print(_ex)
            return False
