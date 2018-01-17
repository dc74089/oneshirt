from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('', include('trade.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
