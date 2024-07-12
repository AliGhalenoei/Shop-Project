from django.contrib import admin

from .models import *
# Register your models here.


class GaleryInline(admin.TabularInline):
    model = GaleryProduct

@admin.register(Product)
class ProdutAdmin(admin.ModelAdmin):
    inlines = [GaleryInline]
    list_display = ['title','status','is_avalable' , 'id']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    prepopulated_fields = {'slug':('title',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'id']
    prepopulated_fields = {'slug':('title',)}