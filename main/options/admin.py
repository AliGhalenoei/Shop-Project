from django.contrib import admin

from .models import Story
# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'id']