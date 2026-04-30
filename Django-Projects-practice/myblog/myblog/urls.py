from django.contrib import admin
from django.urls import path
# from . import views
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.hello),
]
