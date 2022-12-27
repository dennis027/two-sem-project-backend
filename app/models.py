from argparse import _SubParsersAction


import datetime
datetime.datetime.now()
from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from datetime import date, datetime as dt
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    role_choices = (('is_admin','Admin'),('is_professional','Professional'),('is_addict','Addict'))
    role = models.CharField(max_length=20, choices=role_choices,null=False)
    phone = models.IntegerField(blank=False,default=0) 


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class Addict(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username        


class Contact(models.Model):
    id= models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    subject = models.CharField(max_length=60, blank=True)
    message = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now=True,null=True) 

    def __str__(self):
        return f'{self.user.username}'        


class Diagnosis(models.Model):
    id= models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis_subject = models.CharField(max_length=60, blank=True)
    diagnosis_message = models.CharField(max_length=300, blank=True)
    diagnosis_date = models.DateTimeField(auto_now=True,null=True) 

class Recommendations(models.Model):
    diagnosis_id = models.ForeignKey(Diagnosis , on_delete=models.CASCADE)
    id= models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_subject = models.CharField(max_length=60, blank=True)
    recommendation_message = models.CharField(max_length=300, blank=True)
    recommendation_date = models.DateTimeField(auto_now=True,null=True)   


 
class Questions(models.Model):
    id= models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_subject = models.CharField(max_length=60, blank=True)
    question_message = models.CharField(max_length=300, blank=True)
    question_date = models.DateTimeField(auto_now=True,null=True)
  
class Answers(models.Model):
    id= models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey(Questions , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_subject = models.CharField(max_length=60, blank=True)
    answer_message = models.CharField(max_length=300, blank=True)
    answer_date = models.DateTimeField(auto_now=True,null=True)
    
class Testimonies(models.Model):
    id= models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimony_subject = models.CharField(max_length=60, default="Add Subject", blank=True)
    testimony_message = models.TextField(max_length=255,blank=True)
    testimony_location = models.CharField(max_length=60,blank=True)
    testimony_date = models.DateTimeField(auto_now=True,null=True)
    # date = models.DateTimeField(auto_now=True,null=True)

class Approve(models.Model):
    id= models.BigAutoField(primary_key=True)
    testimony_id = models.OneToOneField(Testimonies , on_delete=models.CASCADE ,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approveTF = models.CharField(max_length=1, blank=True )
    approve_date = models.DateTimeField(auto_now=True,null=True)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Mwangaza"),
        # message:
        email_plaintext_message,
        # from:
        "machariad196@gmail.com",
        # to:
        [reset_password_token.user.email]
    )        

def send_email(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = 'thsiodejndjkewbdc'

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Mwangaza"),
        # message:
        email_plaintext_message,
        # from:
        "machariad196@gmail.com",
        # to:
        [reset_password_token.user.email]
    )        


