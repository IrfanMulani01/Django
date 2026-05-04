from django.shortcuts import render
from .forms import StudentModelLoggin

def accept_data(request):
    if request.method == 'POST':
        form = StudentModelLoggin(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
    else:
        form = StudentModelLoggin()
    
    return render(request, 'temp/index.html', {'form':form})