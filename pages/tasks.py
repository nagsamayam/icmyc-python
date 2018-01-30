from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from celery.decorators import task


@task(name="send_test_mail")
def dispatch_mail(to_list, subject, html_content, from_email='example@example.com'):
    msg = EmailMessage(subject, html_content, from_email, [to_list])
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()
