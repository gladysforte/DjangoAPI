from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeViewSet
from employee import views

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename="employee")

urlpatterns = [
    path('', include(router.urls)),
    # path('employee/', views.EmployeeViewSet.as_view())
]