import time
from smtp_mailer import Mailer
from celery import Celery
import os
from dotenv import load_dotenv
load_dotenv()

mail = Mailer(
    sender_email=os.environ.get("SENDER_EMAIL"), sender_password=os.environ.get("SENDER_PASSWORD")
)

celery_app = Celery(
    os.environ.get("CELERY_NAME"), broker=os.environ.get("REDIS_BROKER_URL"), backend=os.environ.get("REDIS_BACKEND_URL")
)


@celery_app.task
def send_mail_by_celery_test(template_path, receiver_mail, subject, **kwargs):
    mail.send_mail(
        template_path=template_path,
        reciever_mail=receiver_mail,
        subject=subject,
        **kwargs,
    )


def demo_mail_by_celery():
    result = send_mail_by_celery_test.delay(
        template_path="mail.html",
        receiver_mail=os.environ.get("RECIEVER_EMAIL"),
        subject="A demo for celery mail",
        type="celery integrated",
    )
    return "Celery configured mail send successfully"
