from django.contrib import admin
from .models import User_Profile

class Cust_admin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_pic', 'create_at']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']

admin.site.register(User_Profile, Cust_admin)