from django.urls import path
from app.api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

list_actions = {
    'get': 'list',
    'post': 'create'
}

detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

employee_list = EmployeeViewSet.as_view(list_actions)
employee_detail = EmployeeViewSet.as_view(detail_actions)

training_list = TrainingViewSet.as_view(list_actions)
training_detail = TrainingViewSet.as_view(detail_actions)

user_permission_list = UserPermissionViewSet.as_view(list_actions)
user_permission_detail = UserPermissionViewSet.as_view(detail_actions)

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('employees/', employee_list, name='employee-list'),
    path('employees/<uuid:id>/', employee_detail, name='employee-detail'),
    path('trainings/', training_list, name='training-list'),
    path('trainings/<uuid:id>/', training_detail, name='training-detail'),
    path('user-permissions/', user_permission_list, name='user-permission-list'),
    path('user-permissions/<uuid:id>/', user_permission_detail, name='user-permission-detail')
])
