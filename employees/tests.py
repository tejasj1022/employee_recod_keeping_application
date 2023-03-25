"""
Tests for the Employee API.

This test case includes tests for creating, retrieving, updating, and deleting
employees using the API.

Attributes:
    client (APIClient): An instance of Django's test client, used to make API requests.
    user (User): A user account used to authenticate API requests.
    employee_data (dict): A dictionary representing data for creating an employee.
    response (Response): A response object returned from a create employee request.

Methods:
    setUp(): Method to set up the test case.
    test_create_employee(): Test method to create an employee using the API.
    test_get_employee_list(): Test method to retrieve a list of employees using the API.
    test_get_employee_detail(): Test method to retrieve an individual employee using the API.
    test_update_employee(): Test method to update an employee using the API.
    test_delete_employee(): Test method to delete an employee using the API.
"""

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeTest(APITestCase):
    """
    Test cases for CRUD operations on Employee model
    """

    def setUp(self):
        """
        Set up test environment and create an authenticated client
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.employee_data = {
            "name": "John Doe",
            "age": 30,
            "gender": "M",
            "department": "A",
            "salary": "5000.00",
        }
        self.response = self.client.post(
            reverse("employee-create"),
            self.employee_data,
            format="json",
        )

    def test_create_employee(self):
        """
        Test case for creating a new employee

        This method tests the creation of a new employee by checking the status
        code of the HTTP response after making a POST request to the "employee-create"
        URL endpoint. It asserts that the status code is `HTTP_201_CREATED`,
        indicating that the employee was successfully created.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_employee_list(self):
        """
        Test case for retrieving a list of employees

        This method tests the retrieval of a list of employees by making a GET
        request to the "employee-list" URL endpoint, retrieving all employees from the
        database, and serializing the data. It asserts that the status code of the HTTP response
        is `HTTP_200_OK`, indicating that the request was successful, and that the
        serialized data of the retrieved employees is equal to the expected serialized data.

        """
        response = self.client.get(reverse("employee-list"))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_detail(self):
        """
        Test case for retrieving the details of a specific employee

        This method tests the retrieval of the details of a specific employee by
        getting the first employee from the database, making a GET request to the
        "employee-detail" URL endpoint with the employee's ID, serializing the employee
        data, and comparing it to the expected serialized data. It asserts that the
        status code of the HTTP response is `HTTP_200_OK`, indicating that the request
        was successful, and that"""
        employee = Employee.objects.first()
        response = self.client.get(
            reverse("employee-detail", kwargs={"pk": employee.id})
        )
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        """
        Test case for updating an existing employee

        This method tests the updating of an existing employee by getting the first
        employee from the database, updating the employee data with new values, making
        a PUT request to the "employee-update" URL endpoint with the updated employee
        data, and comparing the response status code to the expected status code
        `HTTP_200_OK`, indicating that the request was successful.
        """
        employee = Employee.objects.first()
        updated_employee = {
            "name": "Jane Doe",
            "age": 40,
            "gender": "F",
            "department": "S",
            "salary": "7000.00",
        }
        response = self.client.put(
            reverse("employee-update", kwargs={"pk": employee.id}),
            updated_employee,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        """
        Test case for deleting an existing employee

        This method tests the deleting of an existing employee by getting the first
        employee from the database, making a DELETE request to the "employee-delete"
        URL endpoint with the employee's ID, and comparing the response status code
        to the expected status code `HTTP_204_NO_CONTENT`, indicating that the
        request was successful and the resource has been deleted.
        """
        employee = Employee.objects.first()
        response = self.client.delete(
            reverse("employee-delete", kwargs={"pk": employee.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
