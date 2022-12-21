from re import search
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login
from .models import *
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from app.forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError 
from django.http import HttpResponse
from django.contrib import messages
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
# Create your views here.


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user) 
        return super(LoginAPI, self).post(request, format=None)
# def index(request):
    

#     return render (request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):  
    search_fields = ['email','username']
    # filter_backends = (filters.SearchFilter)
    queryset = User.objects.all()
    serializer_class = UserSerializer




'''
    custom api view to post user, generate token, confim token and login users
'''
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "role": user.role,
                "email": user.email,
                "username": user.username,
            }
        )


'''
user view for serilizers
'''   

class ContactViewSet(viewsets.ModelViewSet):
    search_fields=['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer      

class DiagnosisViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisInfoSerializer

class RecommendationsViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsInfoSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Questions.objects.all()
    serializer_class = QuestionsInfoSerializer

class AnswersViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Answers.objects.all()
    serializer_class = AnswersInfoSerializer

class TestimoniesViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Testimonies.objects.all()
    serializer_class = TestimoniesSerializer    

class ApproveViewSet(viewsets.ModelViewSet):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Approve.objects.all()
    serializer_class = ApproveInfoSerializer


def email(request):
    form = ContactMeForm()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)
            subject = "Email Test"
            body = {
                # 'first_name': form.cleaned_data['first_name'],
                # 'last_name':form.cleaned_data['last_name'],
                'email': form.cleaned_data['emailid'],
                # 'phonenumber': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            # message = 'welcome to mwangaza little'
            sender = 'machariad196@gmail.com'
            recipient = form.cleaned_data['emailid'],
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Your respoce has been submited successfully")
    context = {
        'form':form,
    }
    return render(request, "index.html", context)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendMailView(APIView):
    """
    an endpoint for sending emails
    """    
    serializer_class=SendEmails
    model = User
    permission_classes = (IsAuthenticated,)
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def send (self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializers(data=request.data)    

        if serializer.is_valid():
            self.object.send_email(serializer.data.get("emailid","subject","message"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
           