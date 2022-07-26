"""project_2 URL Configuration

The `urlpatterns` list routes URLs to views_erp. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views_erp
    1. Add an import:  from my_app import views_erp
    2. Add a URL to urlpatterns:  path('', views_erp.home, name='home')
Class-based views_erp
    1. Add an import:  from other_app.views_erp import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls'))
]
