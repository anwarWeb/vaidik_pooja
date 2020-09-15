from django.shortcuts import render
from django.http import HttpResponse
from .models import Services,Contact,Book
# Create your views here.

def home(request):
    return render(request, 'vidik/index.html')

def contact_us(request):
    
    return render(request, 'vidik/contact-us.html')

def contactSave(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request,'vidik/contact-us.html',{'message':'Message has been send !'})

def about_us(request):
    return render(request, 'vidik/about.html')

# def services(request):
#     services= Services.objects.all()
#     return render(request,'frontend/services.html',{'services_list':services})

def team(request):
    return render(request,'vidik/team.html')

def services(request):
    services= Services.objects.all()
    return render(request,'vidik/services.html',{'services_list':services})

def servicesView(request,myid):
    services_ls=Services.objects.filter(id=myid)
    return render(request,"frontend/services_view.html",{'services_ls':services_ls[0]})

def orederform(request):
    # services= Services.objects.all()
    return render(request,"vidik/book.html")

def orderSave(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        countryCode=request.POST.get('countryCode', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        pooja_date = request.POST.get('date', '')
        select_pooja = request.POST.get('select_pooja', '')

        book = Book(name=name, email=email,countryCode=countryCode, phone=phone, address=address, pooja_date=pooja_date, select_pooja=select_pooja)
        book.save()
    return render(request,'vidik/book.html',{'message':'Booking is successful!'})
