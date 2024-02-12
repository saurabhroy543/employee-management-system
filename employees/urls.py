from django.urls import path,include
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, add_task
from rest_framework.routers import DefaultRouter
from .viewsets import EmployeeViewSet, EmployeeTaskViewSet,UpdateTaskStatusAPIView

router = DefaultRouter()
router.register(r'get_employees', EmployeeViewSet) # to fetch all the employee
router.register(r'employeetasks', EmployeeTaskViewSet) # To fetch all the task and also search=<emp_id> to fetch task of that employee

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('add-task/', add_task, name='add_task'),
    path('employee/<int:employee_id>/add_task/', add_task, name='add_task'),
    path('update_task_status/<int:pk>/', UpdateTaskStatusAPIView.as_view(), name='update_task_status'), # update status of a task

    path('api/', include(router.urls)),
]