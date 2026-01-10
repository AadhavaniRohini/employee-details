from django.shortcuts import render

# Create your views here.
from .models import employees, department
 
def dashboard(request):
    return render(request, 'dashboard.html',
                  {
                      'employees_count':employees.objects.count(),
                      'departments': department.objects.count()
                  }
                  )
       
def employees_list(request):
    employees_data = employees.objects.all()
    return render(request, 'employees_list.html',
                  {
                      'employees': employees_data
                  }
                  )
def departments_list(request):
    departments_data = department.objects.all()
    return render(request, 'departments_list.html',
                  {
                      'departments': departments_data
                  }
                  )
def employees_detail(request, employee_id):
    employee_data = employees.objects.get(id=employee_id)
    return render(request, 'employee_detail.html',
                  {
                      'employee': employee_data
                  }
                  )
def add_employee(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        age = request.POST['age']
        department_id = request.POST['department']
        department_instance = department.objects.get(id=department_id)
        new_employee = employees(full_name=full_name, age=age, department=department_instance)
        new_employee.save()
    departments_data = department.objects.all()
    return render(request, 'add_employee.html',
                  {
                      'departments': departments_data
                  }
                  )
def add_employees(request):
    if request.method == 'POST':
        employees_name = request.POST['name']
        duration = request.POST['duration']
        new_employee = employees(full_name=employees_name, duration=duration)
        new_employee.save()
    return render(request, 'add_employees.html')
def add_department(request):
    if request.method == 'POST':
        department_name = request.POST['name']
        new_department = department(name=department_name)
        new_department.save()
    return render(request, 'add_department.html')

def department_detail(request, department_id):
    department_instance = department.objects.get(id=department_id)
    employees_in_department = employees.objects.filter(department=department_instance)
    return render(request, 'department_detail.html',
                  {
                      'departments': department_instance , 'employees' : employees_in_department
                  }
                  )

def delete_employee(request, employee_id):
    employee = employees.objects.get(id=employee_id)
    employee.delete()
    return render(request, 'employee_deleted.html', 
                  {'employee_name': employee.full_name})

def delete_departments(request, department_id):
    department_instance = department.objects.get(id=department_id)
    department_instance.delete()
    return render(request, 'departments_deleted.html', 
                  {'departments_name': department_instance.name})

def update_employees(request, employee_id):
    employee = employees.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.full_name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.age = request.POST.get('age')
        department_id = request.POST.get('departments')
        employee.department = department.objects.get(id=department_id)
        employee.save()
    departments = department.objects.all()
    return render(request, 'update_employee.html', 
                  {'employee': employee, 'departments': departments})

def update_departments(request, department_id):
    department_instance = department.objects.get(id=department_id)
    if request.method == 'POST':
        department_instance.name = request.POST.get('name')
        department_instance.save()
    return render(request, 'update_departments.html', 
                  {'departments': department_instance})

    