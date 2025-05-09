from django import forms
from django.contrib.auth.models import User
from userapp.models import userModel
from django_recaptcha.fields import ReCaptchaField

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        # fields = '__all__' [if we want all the fileds]

class userForm1(forms.ModelForm):
    class Meta:
        model = userModel
        fields = ['address','street','city','zipcode','userimg']
    captcha = ReCaptchaField()

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = ['address','street','city','zipcode']
    