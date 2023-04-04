from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from company.models import Employee


class EmployeeFilter(FilterSet):
    surname = CharFilter(method='get_by_surname')
    department = NumberFilter(field_name='department_id')

    class Meta:
        model = Employee
        fields = 'surname', 'department'

    def get_by_surname(self, queryset, name, value):
        return (queryset.filter(surname__istartswith=value).all()
                if value else queryset)
