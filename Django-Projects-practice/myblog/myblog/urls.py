from django.contrib import admin
from django.urls import path, include
# from . import views
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.hello),
    path('product/', include('product.urls')),
]
