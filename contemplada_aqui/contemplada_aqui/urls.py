"""contemplada_aqui URL Configuration

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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from cotas import views
from django.contrib import admin
from cotas.views import CotaAPIView, cotas_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_agent', views.update_agent, name='update_agent'),
    path('', views.index, name='index'),
    path('cotas_list', views.cotas_list, name='cotas_list'),
    path('cotas_json', CotaAPIView.as_view(), name='cotas_json'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
