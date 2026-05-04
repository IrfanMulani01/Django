from django.shortcuts import render
from .forms import AddStudent

def add_stud(request):
    if request.method == 'POST':
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = AddStudent()

    return render(request, 'temp/index.html', {'form':form})