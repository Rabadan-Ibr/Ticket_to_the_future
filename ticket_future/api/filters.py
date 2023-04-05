from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from company.models import Employee


class EmployeeFilter(FilterSet):
    full_name = CharFilter(method='get_by_full_name')
    department = NumberFilter(field_name='department_id')

    class Meta:
        model = Employee
        fields = 'full_name', 'department'

    def get_by_full_name(self, queryset, name, value):
        return (queryset.filter(full_name__contains=value).all()
                if value else queryset)
