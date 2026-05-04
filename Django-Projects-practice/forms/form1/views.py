from django.shortcuts import render
from .forms import StudentModelForm

def student_deatil(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
    else:
        form = StudentModelForm()

    return render(request, 'temp/index.html', {'form': form})