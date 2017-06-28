from django import forms
from .models import Accounts


class CreateAccountForm(forms.ModelForm):
    password=forms.CharField(max_length=10, required=True, widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=10, required=True, widget=forms.PasswordInput)
    email_id = forms.EmailField(max_length=25, required=True)
    class Meta:
        model=Accounts
        fields=('account_no','password','confirm_password','email_id')

class Loginform(forms.ModelForm):
    password=forms.CharField(label="password",max_length=10, required=True, widget=forms.PasswordInput)
    class Meta:
        model=Accounts
        fields=('account_no','password')
