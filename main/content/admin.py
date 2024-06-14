from django.contrib import admin

from .models import *
# Register your models here.


class GaleryInline(admin.TabularInline):
    model = GaleryProduct

@admin.register(Product)
class ProdutAdmin(admin.ModelAdmin):
    inlines = [GaleryInline]
    list_display = ['title','is_avalable']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}