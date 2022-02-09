from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'training', TrainingViewSet, basename='training')
router.register(r'user_permission', UserPermissionViewSet, basename='user_permission')
urlpatterns = router.urls
