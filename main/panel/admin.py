from django.contrib import admin

from .models import *
# Register your models here.



@admin.register(MenuNavbar)
class MenuNavbarAdmin(admin.ModelAdmin):
    list_display = ['title' , 'link' , 'id']
