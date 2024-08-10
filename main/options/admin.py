from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'id']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author' , 'title' ]
    prepopulated_fields = {'slug':('title',)}

@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'message'  , 'is_reply' , 'id']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user' , 'email' , 'subject' , 'is_reply' , 'id']

@admin.register(ReplyContact)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user'  , 'contact']

