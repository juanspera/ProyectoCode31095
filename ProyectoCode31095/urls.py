from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda req: redirect('AppCoderInicio')),
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('UserCoder/', include('UserCoder.urls')),
]
