from celery_mail import demo_mail_by_celery
from mail import send_demo_mail

print(demo_mail_by_celery(), send_demo_mail())
