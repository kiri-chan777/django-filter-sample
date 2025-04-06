from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'hire_date', 'status')
    list_filter = ('department', 'status', 'gender')
    search_fields = ('name', 'employee_id', 'email')
    date_hierarchy = 'hire_date'