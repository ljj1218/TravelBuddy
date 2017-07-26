from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.createUser(request.POST)
        messages.success(request, 'User was created. Please login.')
        return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['name'] = results['user'][0].name
        request.session['username'] = results['user'][0].username
        request.session['user_id'] = results['user'][0].id
        return redirect('/travels')

def logout(request):
    request.session.flush()
    return redirect('/')
