from django.forms import fields
from django import forms
from .models import User_Profile
  
class Update_UserPorfile(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['user', 'bio', 'profile_pic']
        widget = {
            'password' : forms.PasswordInput()
        }

    def clean_password(self):
        pas = self.cleaned_data['password']
        if len(pas) <= 6:
            raise forms.ValidationError("Password must be greater than 6 characters")
        return pas