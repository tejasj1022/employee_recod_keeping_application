from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeePagination(PageNumberPagination):
    """Pagination settings for EmployeeListAPIView"""

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class EmployeeListAPIView(ListAPIView):
    """View to list all employees"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """View to retrieve an employee"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """View to create an employee"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(UpdateModelMixin, RetrieveAPIView):
    """
    View to update an employee.
    This view inherits from UpdateModelMixin and RetrieveAPIView to allow updating of an existing employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        """Handle PUT requests to update an employee"""
        return self.update(request, *args, **kwargs)


class EmployeeDeleteAPIView(DestroyModelMixin, RetrieveAPIView):
    """
    View to delete an employee.
    This view inherits from DestroyModelMixin and RetrieveAPIView to allow deletion of an existing employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        """Handle DELETE requests to delete an employee"""
        return self.destroy(request, *args, **kwargs)
