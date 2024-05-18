from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.core.validators import validate_integer

from .validators import validate_phone
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser , PermissionsMixin):
    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_integer , validate_phone],
        verbose_name='تلفن'
    )
    username = models.CharField(max_length=255,verbose_name='نام کاربری' ,unique=True)

    is_active = models.BooleanField(default=True ,verbose_name ="کاربر فعال است؟") 
    is_admin = models.BooleanField(default=False , verbose_name ="کاربر ادمین باشد (دسترسی به پنل ادمین داشته باشد؟)")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        ordering = ('id',)
        verbose_name = 'کاربر'
        verbose_name_plural = "کاربران"

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None ):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return self.is_admin

