from django.contrib import admin
from django.urls import path, include
from django.conf import settings            # Для получения переменных MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static  # Для подключения путей к медиа файлам

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
