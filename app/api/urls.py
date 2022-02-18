from app.api import views
from django.conf.urls import url

from django.urls import path, include
from app.api import views, apis, urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'employees', apis.EmployeeViewSet, 'employee')
router.register(r'trainings', apis.TrainingViewSet, 'training')
router.register(r'user_permission', apis.UserPermissionViewSet, 'user_permission')

urlpatterns = [
    # url(r'^employees/$', views.Employees.as_view(), name='employees'),
    # url(r'^employees/<uuid:id>/$', views.EmployeesForm.as_view(), name='employees_form'),
    # url(r'^employees_formset/$', views.EmployeesFormset.as_view(), name='employees_formset'),
    # url(r'^trainings/$', views.Trainings.as_view(), name='trainings'),
    path('', include(router.urls))
]
