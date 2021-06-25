# User model
from users.models import User
from smtplib import SMTPException

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# celery logger and task
from backend_test.celery import app
from celery.utils.log import get_task_logger

# Logger celery
logger = get_task_logger(__name__)


@app.task(name="send_welcome_email")
def send_welcome_email(password, user_pk):
    """ Task for send email welcome """
    user = User.objects.get(pk=user_pk)
    subject = 'Welcome @{}! to the internal order management system for employees'.format(
        user.username)
    from_email = 'Internal CornerShop <test-cornershop@cornershop.com>'
    content = render_to_string(
        'email/welcome/account_welcome.html',
        {'password': password, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()