from django.contrib import admin
from aprendices.models import Aprendiz

# Register your models here.

@admin.register(Aprendiz)
class AprendicesAdmin(admin.ModelAdmin):
    list_display = ('identificacion','nombre', 'apellido','email','genero','edad','direccion','tipo_sangre','is_active')
