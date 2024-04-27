from smtp_mailer import Mailer
from tests.utils import mail
import os
from dotenv import load_dotenv
load_dotenv()


def test_a_demo_mail():
    assert (
        mail.send_mail(
            template_path="tests/sample_remplate/mail.html",
            reciever_mail=os.environ.get("RECIEVER_EMAIL"),
            subject="A demo normal mail",
            type="simple",
        )
        == True
    )
