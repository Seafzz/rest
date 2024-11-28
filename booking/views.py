from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from .models import Reservation 
from .forms import ReservationForm

def home(request):
    return render(request, 'booking/home.html')

