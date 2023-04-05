from rest_framework import serializers

from company.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField(read_only=True)
    total_salary = serializers.DecimalField(
        read_only=True,
        decimal_places=3,
        max_digits=10,
    )

    class Meta:
        model = Department
        fields = 'id', 'name', 'director', 'employees_count', 'total_salary'


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
