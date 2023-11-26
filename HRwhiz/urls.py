"""
URL configuration for HRwhiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", views.log_in),
    path('verifyotp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.log_out),
    path("admin/", admin.site.urls),
    # path("linkedin_learning/", redirect('https://www.linkedin.com/learning/')),
    # path("etms/", redirect('https://fidelityinternational.com/')),
    path("employee/",include('employee.urls')),
    path("manager/",include('manager.urls')),
    path("HR/", include('HR.urls'))
]
