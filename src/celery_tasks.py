from celery import Celery
from asgiref.sync import async_to_sync

from src.configg import Config
from src.mail import mail, create_message


c_app = Celery(
    "bookly",
    broker=Config.REDIS_URL,
    backend=Config.REDIS_URL
)


@c_app.task(name="send_email")
def send_email(recipients: list[str], subject: str, body: str):
    
    print("Preparing email...")
    print("Recipients:", recipients)
    print("Subject:", subject)

    message = create_message(
        recipients=recipients,
        subject=subject,
        body=body
    )

    print("Sending email now...")
    async_to_sync(mail.send_message)(message)
    print("Email sent successfully from Celery!")

    return {
        "message": "Email sent successfully",
        "recipients": recipients
    }