"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('empdetails.urls')),
    path('employee/',include('empdetails.urls')),
    path('departments/', include('empdetails.urls')),
    path('employee/<int:employee_id>/', include('empdetails.urls')),
    path('add_employee/', include('empdetails.urls')),
    path('add_department/', include('empdetails.urls')),
    path('department/<int:department_id>/', include('empdetails.urls')),
    path('delete_employee/<int:employee_id>/', include('empdetails.urls')),
    path('delete_department/<int:department_id>/', include('empdetails.urls')), 
    path('employee_deleted/', include('empdetails.urls')),
    path('department_deleted/', include('empdetails.urls')),
    path('employee_detail/', include('empdetails.urls')),
    path('department_detail/', include('empdetails.urls')),
    path('department_list/', include('empdetails.urls')),
    path('department_list/', include('empdetails.urls')),
    path('dashboard/', include('empdetails.urls')),
]