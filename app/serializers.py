
from email import message
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models, transaction
from .models import *
from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import models, transaction
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters

from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
User = get_user_model()
# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = User
        fields =  ['id','username','email','phone','role','password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))
    
        return user   

'''
    registration serializer class
'''
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))
        return user

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','name','email','subject','message')

class PartnerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerInfo
        fields = ('user','subject','message','date')         

class VolunteerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerInfo
        fields = ('user','subject','message','date')                 


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('user','subject','message','location','date')     


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class SendEmails(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    emailid = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)