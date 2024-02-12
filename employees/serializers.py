from rest_framework import serializers
from .models import Employee, EmployeeTask


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTask
        fields = '__all__'


class UpdateTaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTask
        fields = ['status']
