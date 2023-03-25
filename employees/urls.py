from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import EmployeeListAPIView
from .views import EmployeeRetrieveAPIView
from .views import EmployeeCreateAPIView
from .views import EmployeeUpdateAPIView
from .views import EmployeeDeleteAPIView


schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version="v1",
        description="API for managing employees",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
