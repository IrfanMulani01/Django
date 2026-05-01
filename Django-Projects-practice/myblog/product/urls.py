from django.urls import path
from . import views

urlpatterns = [
    path('', views.product),
    path('product_list/', views.product_list),
    path('prod_cat/', views.prod_cat),
]