from django.contrib import admin
from django.db import models
from .models import Categories, CreatePost
from django import forms
# Register your models here.
#class AdminCategories(admin.ModelAdmin):
admin.site.register(Categories)

class AdminCreatePost(admin.ModelAdmin):
    list_display = ('title', 'created')
    ordering = ('title', 'created')
    
    formfield_overrides  = { models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }

admin.site.register(CreatePost, AdminCreatePost)