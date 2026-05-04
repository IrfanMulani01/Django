from django import forms
from .models import StudentLog

class StudentModelLoggin(forms.ModelForm):
    class Meta:
        model = StudentLog
        fields = ['username', 'password']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters")
        return password