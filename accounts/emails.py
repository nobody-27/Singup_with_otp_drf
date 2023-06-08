from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
import pyotp


def send_email_via_email(email):
    subject = f'Your account verification email'
    tootp = pyotp.TOTP(pyotp.random_base32(),interval=60)
    otp = tootp.now()
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
