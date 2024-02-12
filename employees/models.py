from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    identification_document = models.FileField(upload_to='identification_documents/', null=True, blank=True)


class EmployeeTask(models.Model):
    STATUS_CHOICES = [
        ('TO DO', 'To Do'),
        ('HOLD', 'Hold'),
        ('IN PROGRESS', 'In Progress'),
        ('REVIEW', 'Review'),
        ('DONE', 'Done'),
    ]

    TYPE_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    ticket_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO DO')
    reporter = models.ForeignKey(Employee, related_name='reported_tasks', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
