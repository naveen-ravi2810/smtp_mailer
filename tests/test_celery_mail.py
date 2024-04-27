from tests.utils import send_mail_by_celery_test
import time
import os
from dotenv import load_dotenv
load_dotenv()




def test_a_demo_by_celery():
    start_time = time.time()
    result = send_mail_by_celery_test.delay(
        template_path="tests/sample_template/mail.html",
        receiver_mail=os.environ.get("RECIEVER_EMAIL"),
        subject="A demo for celery mail",
        type="celery integrated",
    )

    assert int(time.time() - start_time) <= 1
