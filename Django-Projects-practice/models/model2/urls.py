from django.urls import path 
from . import views

urlpatterns = [
    path('', views.add_prod),
    path('prod_list/', views.disp_prod, name='record'),
]
