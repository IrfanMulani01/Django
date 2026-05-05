from django.contrib import admin
from .models import User, User_Profile

class Cust_admin(admin.ModelAdmin):
    list_display = ['id','user', 'bio', 'profile_pic', 'create_at']
    search_fields = ['user']
    list_filter = ['user']
    ordering = ['id']

class Cust_admin2(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'password']
    ordering = ['id']

admin.site.register(User_Profile, Cust_admin)
admin.site.register(User, Cust_admin2)