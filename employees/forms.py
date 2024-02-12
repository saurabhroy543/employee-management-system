from django import forms
from .models import Employee, EmployeeTask
from django.core.validators import FileExtensionValidator


class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    identification_document = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


class EmployeeTaskForm(forms.ModelForm):
    class Meta:
        model = EmployeeTask
        fields = ['task_name', 'task_description', 'ticket_number', 'status', 'reporter', 'type']
        labels = {
            'task_name': 'Task Name',
            'task_description': 'Task Description',
            'ticket_number': 'Ticket Number',
            'status': 'Status',
            'reporter': 'Reporter',
            'type': 'Type',
        }
        widgets = {
            'task_description': forms.Textarea(attrs={'rows': 4}),
            'status': forms.Select(choices=EmployeeTask.STATUS_CHOICES),
            'reporter': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(choices=EmployeeTask.TYPE_CHOICES),
        }