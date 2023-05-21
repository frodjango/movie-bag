#~/movie-bag/services/mail_service.py
from flask import current_app

from threading import Thread
from flask_mail import Message
from app.resources.errors import InternalServerError

# from app import app
# from app import mail

def send_async_email(app, msg):
    pass
    # with app.app_context:
    #     try:
    #         app.mail.send(msg)
    #     except ConnectionRefusedError:
    #         raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    pass
    # msg = Message(subject, sender=sender, recipients=recipients)
    # msg.body = text_body
    # msg.html = html_body

    # Thread(target=send_async_email, args=(current_app, msg)).start()
