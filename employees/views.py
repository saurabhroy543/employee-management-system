from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
from .forms import EmployeeForm, EmployeeTaskForm
from .models import Employee


class EmployeeListView(View):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees_employee")
            employees = dictfetchall(cursor)
        return render(request, 'employees/employee_list.html', {'employees': employees})


class EmployeeDetailView(View):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees_employee WHERE id = %s", [pk])
            employee = dictfetchone(cursor)
            cursor.execute("SELECT * FROM employees_employeetask WHERE employee_id = %s", [pk])
            tasks = dictfetchall(cursor)
        return render(request, 'employees/employee_detail.html', {'employee': employee, 'tasks': tasks})



class EmployeeCreateView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employees/employee_form.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['identification_document']
            if not file.name.endswith('.pdf'):
                error_message = 'Only PDF files are allowed.'
                return render(request, 'employees/employee_form.html', {'form': form, 'error_message': error_message})
            file_content = form.cleaned_data['identification_document'].read()
            file_path = default_storage.save('identification_documents/employee_file.pdf', ContentFile(file_content))

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO employees_employee (first_name, last_name, email, identification_document) "
                    "VALUES (%s, %s, %s, %s)",
                    [form.cleaned_data['first_name'], form.cleaned_data['last_name'],
                     form.cleaned_data['email'], file_path]
                )
            return redirect('employee_list')
        return render(request, 'employees/employee_form.html', {'form': form})


def add_task(request,employee_id):
    if request.method == 'POST':
        form = EmployeeTaskForm(request.POST)
        if form.is_valid():
            employee = Employee.objects.get(pk=employee_id)
            task = form.save(commit=False)
            task.employee = employee
            task.save()
            return redirect('employee_detail', pk=employee_id)
    else:
        form = EmployeeTaskForm()
    return render(request, 'add_task.html', {'form': form})

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))
