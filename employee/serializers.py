from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'password', 'address', 'phone_number', 'pid', 'did', 'manager_id', 'status', 'profile_url')
