from django.urls.conf import path,include
from . import views
from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import ChangePasswordView
from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *  
# from rest_framework_jwt.views import obtain_jwt_token 

router = DefaultRouter()

router.register('user',UserViewSet,basename='user'),
router.register('contact',ContactViewSet,basename='contact')
router.register('diagnosisAPI',DiagnosisViewSet,basename='diagnosisAPI')
router.register('questionsAPI',QuestionsViewSet,basename='questionsAPI')
router.register('testimoniesAPI',TestimoniesViewSet,basename='testimoniesAPI')

urlpatterns=[
     path('',include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),               
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
     path('token/',CustomAuthToken.as_view(),name='token'),
       path('email',views.email,name='email'),     
          path('api/change-password/', ChangePasswordView.as_view(), name='change-password'), 
            path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('sendmail/',SendMailView.as_view(),name='sendmail'),
    

] 