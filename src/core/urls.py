from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # WEB
    path('api/', include('mainapp.urls')),

    # API
    path('phone_api/', include('mainapp.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
