"""Mailer class to perform actions"""

from pathlib import Path


from.basic import send_mail_temp


class Mailer:
    def __init__(
        self,
        *,
        sender_email: str,
        sender_password: str,
        server: str | None = "smtp.gmail.com",
        server_port: int | None = 587,
    ):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.server = server
        self.server_port = server_port

    def send_mail(
        self, *, template_path: Path, reciever_mail: str, subject: str, **kwargs
    ) -> bool:
        return send_mail_temp(
            template_path=template_path,
            reciever_mail=reciever_mail,
            subject=subject,
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            server=self.server,
            server_port=self.server_port,
            **kwargs,
        )
