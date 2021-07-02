from django.contrib import admin
from .models import Cap
# Register your models here.

class AdminCap(admin.ModelAdmin):   
    list_display = ( "title", "numeroCapitulo", "created")
    ordering = ("title", "created")

admin.site.register(Cap, AdminCap)