import uuid
from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())  # editable=False
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    position = models.CharField(max_length=256)
    sex = models.BooleanField()
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee'
        ordering = ['created_at', 'updated_at']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Training(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_training_set')
    language = models.CharField(max_length=128)
    speaking = models.IntegerField()
    listening = models.IntegerField()
    writing = models.IntegerField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='created_by_training_set')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='updated_by_training_set')

    class Meta:
        db_table = 'training'
        ordering = ['created_at', 'updated_at']


class UserPermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    is_admin = models.BooleanField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='user_permission_employee_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_permission'
        ordering = ['created_at', 'updated_at']
