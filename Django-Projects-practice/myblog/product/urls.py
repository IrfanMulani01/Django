from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.product),
    path('product_list/', views.product_list),
    path('prod_cat/', views.prod_cat),
    path('student/<int:id>/', views.Student_detail),
    path('product/<str:name>/', views.product_detail),
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year),
]