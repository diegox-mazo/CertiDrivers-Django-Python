from django.contrib import admin
from instructores.models import Instructor

# Register your models here.

@admin.register(Instructor)
class InstructoresAdmin(admin.ModelAdmin):
    list_display = ('identificacion','nombre', 'apellido','email','telefono','profile_picture','is_active')
    
