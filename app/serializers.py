
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
        fields = ('id','name','email','subject','message','date')

class DiagnosisInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id','user','drug','diagnosis_subject','diagnosis_message','diagnosis_date')         

class RecommendationsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ('id','diagnosis_id','user','recommendation_subject','recommendation_message','recommendation_date')             

class QuestionsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id','user','question_subject','question_message','question_date')                 
class AnswersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id','question_id','user','answer_subject','answer_message','answer_date')      

class TestimoniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonies
        fields = ('id','user','testimony_subject','testimony_message','testimony_location','testimony_date')     

class ApproveInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approve
        fields = ('id','testimony_id','user','approveTF','approve_date')     
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

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField()
    from_email = serializers.EmailField()
    recipient_list = serializers.ListField(child=serializers.EmailField())