from django.contrib import admin
from .models import Services, Pandit ,Contact, Book
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    readonly_fields = ('thumbnail_preview',)


    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Services, ServicesAdmin)


class PanditAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'age')

admin.site.register(Pandit, PanditAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','message')

admin.site.register(Contact, ContactAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','countryCode', 'phone','address','pooja_date','select_pooja')
admin.site.register(Book, BookAdmin)