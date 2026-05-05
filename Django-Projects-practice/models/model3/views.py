from django.shortcuts import render
from .forms import Add_user,Update_UserPorfile
from .models import User_Profile

def add_user(request):
    if request.method == 'POST':
        form = Add_user(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Add_user()

    return render(request, 'temp/userAdd.html', {'form': form})


def update_pro(request):
    obj = User_Profile.objects.get(id=1) 
    if not obj:
        return render(request, 'temp/error.html', {'msg': 'Profile not found'})

    if request.method == 'POST':
        form = Update_UserPorfile(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Update_UserPorfile(instance=obj)
    
    return render(request, 'temp/index.html', {'form': form})
