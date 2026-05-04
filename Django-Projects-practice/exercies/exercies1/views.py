from django.shortcuts import render
from .forms import StudentModelForm

def add_student(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
    else:
        form = StudentModelForm()

    return render(request, 'temp/student_form.html', {'form': form})