from django.db import models
from django.core.validators import MaxValueValidator

from djmoney.models.fields import MoneyField


class Employee(models.Model):
    """
    A model to represent an employee.

    Attributes:
        name (CharField): The name of the employee.
        gender (CharField): The gender of the employee.
        age (IntegerField): The age of the employee.
        department (CharField): The department of the employee.
        salary (MoneyField): The salary of the employee.

    Methods:
        __str__(): Returns the name of the employee as a string.

    """

    MALE = "M"
    FEMALE = "F"
    TRANSGENDER = "T"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (TRANSGENDER, "Transgender"),
    ]

    PRODUCTION = "P"
    ADMIN = "A"
    TESTING = "T"
    SALES = "S"
    DEPARTMENT_CHOICES = [
        (PRODUCTION, "Production"),
        (ADMIN, "Admin"),
        (TESTING, "Testing"),
        (SALES, "Sales"),
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(validators=[MaxValueValidator(60)])
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES)
    salary = MoneyField(max_digits=10, decimal_places=2, default_currency="INR")

    def __str__(self):
        """
        Returns the name of the employee as a string.

        Returns:
            str: A string representing the name of the employee.
        """
        return str(self.name)
