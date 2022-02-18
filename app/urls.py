"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.api import views, apis, urls
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'employees', apis.EmployeeViewSet, 'employee')
# router.register(r'trainings', apis.TrainingViewSet, 'training')
# router.register(r'user_permission', apis.UserPermissionViewSet, 'user_permission')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', views.Login.as_view(), name='login'),
    # path('', views.Home.as_view(), name='home'),
    # path('index/', include(urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    # path('login/', views.Login.as_view(), name='login'),
    path('api/v1/', include('app.api.urls'))

]
