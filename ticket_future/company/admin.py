from django.contrib import admin

from company.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'name', 'director'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = 'surname', 'name', 'patronymic'
    search_fields = 'surname',
