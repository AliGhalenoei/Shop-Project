from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User , OTP
from .forms import UserChangeForm , UserCreationForm


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['phone' , 'username' , 'is_admin' ]
    list_filter = ['is_admin']
    search_fields = ['username' , 'phone']
    filter_horizontal = ()
    ordering = ('-id',)

    fieldsets = (
        ('جزئیات کاربر' , {'fields':('phone','username','password')}),
        ('دسترسی ها' , {'fields':('is_admin','is_superuser','is_active')}),
    )

    add_fieldsets = (
        ('Create Account' , {'fields':('phone','username','password','password2')}),
    )
admin.site.register(User,UserAdmin)

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['phone' , 'code']