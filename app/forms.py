
from django import forms
from django.contrib.auth import get_user_model
class ContactMeForm(forms.Form):
    emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter email id'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Message'}), required=True) 