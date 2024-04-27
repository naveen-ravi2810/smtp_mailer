from smtp_mailer import Mailer

mail = Mailer(
    sender_email=os.environ.get("SENDER_EMAIL"), sender_password=os.environ.get("SENDER_PASSWORD")
)


def send_demo_mail():
    mail.send_mail(
        template_path="tests/sample_remplate/mail.html",
        receiver_mail=os.environ.get("RECIEVER_EMAIL"),
        subject="A demo normal mail",
        type="simple",
    )
    return "Normal mail send successfully"
