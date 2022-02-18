from django.views.generic import TemplateView, UpdateView
from .serializers import *
from .forms import *
from rest_framework import viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import sys

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'employee': reverse('employees', request=request, format=format),
        'training': reverse('trainings', request=request, format=format),
        'user_permission': reverse('user_permissions', request=request, format=format)
    })


def login(request):
    if request.method == 'POST':
        usn = request.POST['username']
        pwd = request.POST['password']
        user = UserPermission.objects.filter(username=usn, password=pwd).first()
        print('abc')
        if user:
            user_login = UserPermission.objects.get(username=usn)
            request.session['user_login'] = {
                'username': user_login.username,
                'email': user_login.email,
                'last_name': user_login.employee.last_name,
                'first_name': user_login.employee.first_name,
                'is_admin': user_login.is_admin,
            }
            print(request.session['user_login'])
            return render(request, 'app/home.html', {'user_login': user_login})
        else:
            messages.error(request, 'Dang nhap that bai.')
    return render(request, 'app/login.html')


def logout(request):
    # if request.method == 'POST':
    if 'user_login' in request.session:
        # print(request.session)
        del request.session['user_login']
    return render(request, 'app/login.html')

# class Login(TemplateView):
#     template_name = 'app/login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

# @login_required(login_url='/app/login/')
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     print(username)
#     return render(request, 'app/login.html')


# def handle_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         check_account = UserPermission.objects.filter().first()
#         # if check_account:


# class Home(TemplateView):
#     template_name = 'app/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         trainings = Training.objects.all()
#         context['trainings'] = trainings
#
#         return context


# class Employees(TemplateView):
#     template_name = 'app/employees.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         employees = Employee.objects.all()
#         context['employees'] = employees
#
#         employee_class = Employee
#         context['employee_class'] = employee_class
#
#         return context
#
#
# class EmployeesForm(UpdateView):
#     template_name = "app/employees_form.html"
#     model = Employee
#     fields = '__all__'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         employee_class = Employee
#         context['employee_class'] = employee_class
#
#         context['knockout_form'] = EmployeeForm(instance=self.object)
#
#         context['form'].fields['ignored'].label += ' (No bindings)'
#
#         return context
#
#     def get_success_url(self):
#         self.success_url = reverse('employees_form',
#                                    kwargs={'pk': self.object.pk})
#
#         return self.success_url
#
#
# class EmployeesFormset(FormsetUpdateView):
#     template_name = "app/employees_formset.html"
#     model = Employee
#
#     def get_success_url(self):
#         self.success_url = reverse('employees_formset')
#
#         return self.success_url
#
#
# class Trainings(TemplateView):
#     template_name = 'app/trainings.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         trainings = Training.objects.all()
#         context['trainings'] = trainings
#
#         training_class = Trainings
#         context['training_class'] = training_class
#
#         return context
#
#
# class UserPermissions(TemplateView):
#     template_name = 'app/user_permissions.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         user_permissions = UserPermission.objects.all()
#         context['user_permissions'] = user_permissions
#
#         user_permission_class = UserPermission
#         context['user_permission_class'] = user_permission_class
#
#         return context
