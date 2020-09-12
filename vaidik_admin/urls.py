from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact-us', views.contact_us, name="contact_us"),
    path('about-us', views.about_us, name="about_us"),
    path('services', views.services, name="services"),
]