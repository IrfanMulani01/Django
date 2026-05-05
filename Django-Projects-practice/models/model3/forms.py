from django.forms import fields
from django import forms
from .models import User, User_Profile

class Add_user(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password']
        widget = {
            'password':forms.PasswordInput()
        }

    def clean_password(self):
        pas = self.cleaned_data['password']
        if len(pas) <= 6:
            raise forms.ValidationError("Password must be greater than 6 characters")
        return pas
    
class Update_UserPorfile(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['user', 'bio', 'profile_pic'] 
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }


class User_profile(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=100)
    profile_pic = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
