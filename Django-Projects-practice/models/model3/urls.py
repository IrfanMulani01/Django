from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user),
    path('update_profile/', views.update_pro),
    path('user/', views.user_pro),
]
