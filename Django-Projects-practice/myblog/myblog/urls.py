from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.hello),
    path('product/', include('product.urls')),
    path('teacher/', include('teacher.urls')),
    path('account/', include('account.urls')),

]
