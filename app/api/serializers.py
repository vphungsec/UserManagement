from rest_framework import serializers
from app.api.models import Employee, Training, UserPermission


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # read_only_fields = ['id']


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'
        extra_kwargs = {'is_admin': {'default': False}}
