from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employees_list, name='employees_list'),
    path('departments/', views.departments_list, name='departments_list'),
    path('employees/<int:employee_id>/', views.employees_detail, name='employee_detail'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_department/', views.add_department, name='add_department'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('delete_departments/<int:department_id>/', views.delete_departments, name='delete_departments'),
    path('update_employee/<int:employee_id>/', views.update_employees, name='update_employee'),
    path('update_departments/<int:department_id>/', views.update_departments, name='update_departments'),

]