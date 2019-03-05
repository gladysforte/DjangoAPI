from rest_framework import serializers
from employee.models import Employee  # from path import class, function


class EmployeeSerializer(serializers.ModelSerializer):  # Pascal(
    class Meta:
        model = Employee
        fields = ('id', 'name', 'age', 'address', 'date_created',
                  'date_updated')
