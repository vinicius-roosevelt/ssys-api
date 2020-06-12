from rest_framework import serializers
from .models import Employee


from datetime import datetime

class EmployeeSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary','birth_date']