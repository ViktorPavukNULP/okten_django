from utils.email_util import EmailUtils

from okten_django.celery import app


@app.task
def spam_email():
    EmailUtils.email_spam()