from django.shortcuts import render, redirect
from .models import Travel
from ..login_app.models import User
from django.contrib import messages


def checkUser(request):
	try:
		if request.session['username'] < 3:
			return False
		else:
			return True
	except:
		return False

def index(request):
    result = checkUser(request)
    if result == False:
        return redirect('/')
    id = request.session['user_id']
    user = User.objects.get(id=id)
    context = {
        'travels': Travel.objects.all(),
        'others': Travel.objects.all().exclude(planedby=user)
    }
    return render(request, 'travel_app/index.html', context)

def addform(request):
    result = checkUser(request)
    if result == False:
        return redirect('/')
    return render(request, 'travel_app/addtravel.html')

def add(request):
    result = checkUser(request)
    if result == False:
        return redirect('/')
    results = Travel.objects.createTrip(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return render(request, 'travel_app/addtravel.html')
    id = request.session['user_id']
    user = User.objects.get(id=id)
    print (request.POST['datefrom'])
    Travel.objects.create(destination = request.POST['destination'], planedby = user, datefrom = request.POST['datefrom'],dateend = request.POST['dateend'],plan = request.POST['plan'])
    return redirect('/travels')

def destination(request,id):
    result = checkUser(request)
    if result == False:
        return redirect('/')
    context = {
        'travel': Travel.objects.get(id=id)
    }
    return render(request, 'travel_app/destination.html', context)




