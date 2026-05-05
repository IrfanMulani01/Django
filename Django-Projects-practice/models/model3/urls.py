from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user),
    path('update_profile/', views.update_pro),
]
