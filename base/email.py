from django.conf import settings
from django.core.mail import send_mail



def send_activation_email(email,email_token):
    subject = 'Account Verification Email'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi,Click on the link to activate your Account http://127.0.0.1:8000/activate/{email_token}'
    email=[email]
    send_mail(subject,message,email_from,email)