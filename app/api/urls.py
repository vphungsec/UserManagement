from django.urls import path, include
from app.api import apis
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', apis.EmployeeViewSet, 'employee')
router.register(r'trainings', apis.TrainingViewSet, 'training')
router.register(r'user_permission', apis.UserPermissionViewSet, 'user_permission')

urlpatterns = [
    path('', include(router.urls))
]
