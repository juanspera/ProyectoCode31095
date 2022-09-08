from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', lambda req: redirect('AppCoderInicio')),
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('UserCoder/', include('UserCoder.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
