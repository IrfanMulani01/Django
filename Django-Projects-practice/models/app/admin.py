from django.contrib import admin
from .models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'age']
    search_fields = ['name']
    list_filter = ['id']
    ordering = ['id']
    readonly_fields = ['age']

admin.site.register(Student, StudentAdmin)