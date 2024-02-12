from rest_framework import viewsets, generics
from .models import Employee, EmployeeTask
from .serializers import EmployeeSerializer, EmployeeTaskSerializer, UpdateTaskStatusSerializer
from rest_framework import filters


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeTaskViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTask.objects.all()
    serializer_class = EmployeeTaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['employee__id']


class UpdateTaskStatusAPIView(generics.UpdateAPIView):
    queryset = EmployeeTask.objects.all()
    serializer_class = UpdateTaskStatusSerializer
