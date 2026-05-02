from django.contrib import admin
from .models import product, Prod_review, Users, User_profile, Course, Student


# one to many relationship
admin.site.register(product)
admin.site.register(Prod_review)

# one to one relationship
admin.site.register(User_profile)
admin.site.register(Users)


# Many to many relationship
admin.site.register(Course)
admin.site.register(Student)