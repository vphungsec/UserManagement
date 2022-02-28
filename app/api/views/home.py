from app.api.models import *
from django.shortcuts import render, redirect


def index(request):
    if 'user_id' in request.session:
        user = UserPermission.objects.get(id=request.session['user_id'])
        trainings = Training.objects.filter(employee=user.employee.id)
        if user and trainings:
            context = {
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_admin': user.is_admin,
                    'employee': user.employee
                },
                'trainings': trainings
            }
            return render(request, "app/index.html", context)
    return redirect('login')
