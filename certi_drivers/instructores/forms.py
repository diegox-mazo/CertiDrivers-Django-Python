from django import forms
from instructores.models import Instructor
    

class InstructoresForm (forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('identificacion','nombre', 'apellido','email','telefono','profile_picture')