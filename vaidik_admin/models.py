from django.db import models
from django.utils.html import mark_safe
# Create your models here.
class Services(models.Model):
    name= models.CharField(max_length=50,default="")
    description=models.TextField(default="")
    price=models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="images/",default="")

    def __str__(self):
        return self.name

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""

class Pandit(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 11)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=30 ,default="")
    email = models.CharField(max_length = 50, default="")
    phone = models.CharField(max_length = 11 ,default="")
    pooja_date = models.DateField(auto_now=False, auto_now_add=False, default="")
    services = models.ForeignKey(Services, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.name