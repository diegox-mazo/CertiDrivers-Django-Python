from django import forms
from aprendices.models import Aprendiz
    

class AprendicesForm (forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ('identificacion','nombre', 'apellido','email','genero','edad','direccion','tipo_sangre')