from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
import datetime
from accounts.manager import UserManager
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=200,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + '' + self.last_name
    
    def __str__(self) -> str:
        return self.email
    

class File_Form(models.Model):
    name = models.CharField(max_length=100,null=True)
    document = models.FileField(upload_to='user_document/')

    def __str__(self) -> str:
        return f'{self.name} Doc_Path {self.document.name.capitalize()}'
