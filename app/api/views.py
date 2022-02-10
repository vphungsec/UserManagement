from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'employee': reverse('employee-list', request=request, format=format),
        'training': reverse('training-list', request=request, format=format)
    })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
