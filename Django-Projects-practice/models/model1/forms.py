from django import forms
from .models import Student

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'course']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Age must be 18 or 18 + ")
        return age
    