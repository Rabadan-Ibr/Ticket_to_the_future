from rest_framework import serializers

from company.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = 'id', 'name', 'director', 'employees_count', 'total_salary'

    def get_total_salary(self, obj):
        return sum(employees.salary for employees in obj.employees.all())

    def get_employees_count(self, obj):
        return obj.employees.count()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'surname',
            'patronymic',
            'photo',
            'appointment',
            'salary',
            'age',
            'department',
        )
