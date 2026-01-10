from django.contrib import admin

# Register your models here.
from.models import department, employees
 
admin.site.register(employees)
admin.site.register(department)