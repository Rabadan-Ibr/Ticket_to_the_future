from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import DepartmentViewSet, EmployeeViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('department', DepartmentViewSet, basename='department')
router_v1.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('auth/token/login', views.obtain_auth_token),
]
