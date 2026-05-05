from django.shortcuts import render
from .forms import Add_user,Update_UserPorfile, User_profile
from .models import User_Profile, User

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
    if request.method == 'POST':
        form = Update_UserPorfile(request.POST, request.FILES)
        
        if form.is_valid():
            profile = form.save(commit=False)
            
            # Automatically assign a user (temporary solution)
            user_obj = User.objects.first()  # or filter by username etc.
            if not user_obj:
                user_obj = User.objects.create(
                    name="Test User", 
                    username="testuser", 
                    password="password123"
                )
            
            profile.user = user_obj
            profile.save()
            
            return render(request, 'temp/success.html')
    else:
        form = Update_UserPorfile()

    return render(request, 'temp/index.html', {'form': form})


def user_pro(request):
    user = User_Profile.objects.all()
    return render(request, 'temp/userProfile.html', {'user': user})