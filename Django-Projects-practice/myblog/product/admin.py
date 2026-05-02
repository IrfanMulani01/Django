from django.contrib import admin
from .models import product, Prod_review, User_profile

admin.site.register(product)

admin.site.register(Prod_review)

admin.site.register(User_profile)