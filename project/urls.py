"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path

admin.sites.AdminSite.site_header = 'CalCalC'
admin.sites.AdminSite.site_title = 'CalCalC Admin Portal'
admin.sites.AdminSite.index_title = 'Welcome to CalCalC'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mealplanmaker.urls")),
]
