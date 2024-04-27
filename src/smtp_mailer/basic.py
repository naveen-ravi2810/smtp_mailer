from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail_temp(
    *,
    template_path: Path,
    reciever_mail: str,
    subject: str,
    sender_email,
    server: str,
    server_port: int,
    sender_password: str,
    **kwargs,
):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = reciever_mail
    msg["Subject"] = subject

    template_path = Path(template_path)

    with template_path.open(mode="r", encoding="utf-8") as file:
        template = file.read()
        if kwargs:
            for index, key in enumerate(kwargs):
                template = template.replace("{{" + key + "}}", str(kwargs[key]))
            msg.attach(MIMEText(template, "html"))

    with smtplib.SMTP(host=server, port=server_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever_mail, msg.as_string())
    return True
