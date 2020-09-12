from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'frontend/home.html')

def contact_us(request):
    return render(request, 'frontend/contact_us.html')

def about_us(request):
    return render(request, 'frontend/about_us.html')

def services(request):
    return render(request, 'frontend/services.html')