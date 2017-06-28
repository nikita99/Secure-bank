from django import forms
from .models import Signup


class Signupform(forms.ModelForm):
    password=forms.CharField(max_length=10, required=True, widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=10, required=True, widget=forms.PasswordInput)
    email_id = forms.EmailField(max_length=25, required=True)
    class Meta:
        model=Signup
        fields=('company_name','license_id','city','password','confirm_password','email_id')

class Loginform(forms.ModelForm):
    password=forms.CharField(label="password",max_length=10, required=True, widget=forms.PasswordInput)
    class Meta:
        model=Signup
        fields=('company_name','password')
