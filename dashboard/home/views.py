from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User

from qr_ticket.models import *
from crowd_status.models import *

# Create your views here.
@login_required(login_url='login')
def home_index(request):
    UserTravelHistory = TicketHistory.objects.filter(user = request.user)

    StationsList = StationInfo.objects.all()

    return render(request, 'home/index.html', {
        'history' : UserTravelHistory,
        'stationList' : StationsList
    })

def loginUser(request):
    print(request)

    message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next','home_index'))
            return redirect('home_index')

        else:
            message = 'Wrong Credentials'

    return render(request, 'home/login.html', {
        'message': message,
        'page': 'login'
    })

@login_required(login_url='login')
def logoutUser(request):
    return HttpResponse('Logout')

def registerUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 and password2 and password1 != password2:
            return render(request, 'home/login.html',{
                'page': 'register',
                'message': 'Passwords do not match',
            })
        user = User.objects.create_user(username=username,password=password1)
        user.save()

        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home_index')


    return render(request, 'home/login.html',{
        'page': 'register',
    })