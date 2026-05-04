from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.hello),
    path('product/', include('product.urls')),
    path('teacher/', include('teacher.urls')),
    path('account/', include('account.urls')),
    path('temp/', include('Fortemplate.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)