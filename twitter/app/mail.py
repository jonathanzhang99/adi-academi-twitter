from flask import current_app, render_template
from flask_mail import Message
from threading import Thread
from . import mail


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, template, to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_HEADER'] + subject,
                  sender=('Jonathan Zhang', app.config['MAIL_USERNAME']),
                  recipients=[to],
                  body=render_template(template + '.txt', **kwargs),
                  html=render_template(template + '.html', **kwargs))
    thr = Thread(target=send_async_mail, args=(app, msg))
    thr.start()
