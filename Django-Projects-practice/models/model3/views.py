from django.shortcuts import render
from django.template.context_processors import request
from .forms import Add_user, Update_UserPorfile

def add_user(request):
    if request.method == 'POST':
        form = Add_user(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Add_user()

    return render(request, 'temp/index.html', {'form': form})


def update_pro(request):
    if request.method == 'POST':
        form = Update_UserPorfile(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Update_UserPorfile()
    
    return render(request, 'temp/form2.html')
