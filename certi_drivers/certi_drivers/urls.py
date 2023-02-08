"""certi_drivers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from certi_drivers.views import vista_index, vista_about, vista_licencias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', vista_index, name='index'),
    path('about/', vista_about, name='about'),
    path('licencias/', vista_licencias, name='licencias'),
    path('admin/', admin.site.urls),    

    path('aprendices/', include('aprendices.urls')),
    path('instructores/', include('instructores.urls')),
    path('users/', include('users.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
