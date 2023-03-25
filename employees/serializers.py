from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.
    This serializer is used to convert Employee model instances to JSON format.
    """

    class Meta:
        """
        Metadata for ExampleSerializer.
        This class specifies the model to use, the fields to include, and any extra options.
        """

        model = Employee
        fields = "__all__"
