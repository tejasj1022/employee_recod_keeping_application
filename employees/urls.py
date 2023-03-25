from django.urls import path

from .views import EmployeeListAPIView
from .views import EmployeeRetrieveAPIView
from .views import EmployeeCreateAPIView
from .views import EmployeeUpdateAPIView
from .views import EmployeeDeleteAPIView

urlpatterns = [
    path("employees/", EmployeeListAPIView.as_view(), name="employee-list"),
    path(
        "employees/<int:pk>/", EmployeeRetrieveAPIView.as_view(), name="employee-detail"
    ),
    path("employees/create/", EmployeeCreateAPIView.as_view(), name="employee-create"),
    path(
        "employees/update/<int:pk>/",
        EmployeeUpdateAPIView.as_view(),
        name="employee-update",
    ),
    path(
        "employees/delete/<int:pk>/",
        EmployeeDeleteAPIView.as_view(),
        name="employee-delete",
    ),
]
