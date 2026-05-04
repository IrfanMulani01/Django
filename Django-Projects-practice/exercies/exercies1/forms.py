from django import forms
from .models import Student


class StudenForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 18:
            raise forms.ValidationError("age must be 18 or 18+")
        return age
    
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email', 'password']
        widget =  {
            'password' : forms.PasswordInput()
        }

    def clean_roll(self):
        roll = self.cleaned_data['roll']
        if roll <= 0:
            raise  forms.ValidationError("Age must be in positive")
        return roll