from app.api.models import *
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect


def login(request):
    if 'user_id' in request.session:
        return redirect('home')

    if request.method == 'POST':
        usn = request.POST['username']
        pwd = request.POST['password']
        user = UserPermission.objects.filter(username=usn, password=pwd).first()
        if user:
            request.session['user_id'] = str(user.id)
            return redirect('home')   # return render(request, 'app/home.html', {'user_login': user_login})
        else:
            messages.error(request, 'Dang nhap that bai.')
    return render(request, 'app/auth.html')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')
