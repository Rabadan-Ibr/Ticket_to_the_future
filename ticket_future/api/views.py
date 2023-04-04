from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.filters import EmployeeFilter
from api.serializers import DepartmentSerializer, EmployeeSerializer
from company.models import Department, Employee


class DepartmentViewSet(ListModelMixin, GenericViewSet):
    queryset = Department.objects.prefetch_related('employees')
    serializer_class = DepartmentSerializer


class EmployeeViewSet(
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Employee.objects
    serializer_class = EmployeeSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = DjangoFilterBackend,
    filterset_class = EmployeeFilter
    permission_classes = IsAuthenticated,
