from django.shortcuts import render
from django.http import HttpResponse
from .models import Services,Contact,Order
# Create your views here.

def home(request):
    return render(request, 'frontend/home.html')

def contact_us(request):
    return render(request, 'frontend/contact_us.html')

def contactSave(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request,'frontend/contact_us.html',{'message':'Message have been send !'})

def about_us(request):
    return render(request, 'frontend/about_us.html')

def services(request):
    services= Services.objects.all()
    return render(request,'frontend/services.html',{'services_list':services})

def servicesView(request,myid):
    services_ls=Services.objects.filter(id=myid)
    return render(request,"frontend/services_view.html",{'services_ls':services_ls[0]})

def orederform(request):
    services= Services.objects.all()
    return render(request,"frontend/order_form.html",{'services':services})

def orderSave(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        pooja_date = request.POST.get('pooja_date', '')
        service = request.POST.get('service', '')

        print(name)
        print(email)
        print(phone)
        print(pooja_date)
        print(service)
        order = Order(name=name, email=email, phone=phone,pooja_date=pooja_date,services_id=service)
        order.save()
    return render(request,'frontend/order_form.html',{'message':'Message have been send !'})
