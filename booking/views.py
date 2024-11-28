from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from .models import Reservation 
from .forms import ReservationForm

def home(request):
    return render(request, 'booking/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            user = form.save()
            login(request, user)
            return redirect('reservation_list')
    else:
        form = UserCreationForm()
    return render(request, 'booking/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'booking/login.html', {'error: Invalid credentials'})
        return render(request, 'booking/login.html')

def logout_view(request):
    logout(request)
    retun redirect('home')