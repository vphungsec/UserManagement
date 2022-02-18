from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from knockout.metadata import KnockoutMetadata


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    metadata_class = KnockoutMetadata
    # authentication_classes = SessionAuthentication
    permission_classes = [IsAuthenticated]


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    metadata_class = KnockoutMetadata
    # authentication_classes = SessionAuthentication
    permission_classes = [IsAuthenticated]


class UserPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    metadata_class = KnockoutMetadata
    # authentication_classes = SessionAuthentication
    permission_classes = [IsAuthenticated]
