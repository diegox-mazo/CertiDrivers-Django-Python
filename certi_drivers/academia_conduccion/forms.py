from django import forms

class   AprendicesForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    tipo_sangre = forms.CharField(max_length=3)

class InstructoresForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    jornada = forms.CharField(max_length=50)


class VehiculosForm (forms.Form):
    tipo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    placa = forms.CharField(max_length=10)


class LicenciasForm (forms.Form):
    clasificacion = forms.CharField(max_length=2)
    descripcion = forms.CharField(max_length=100)
    vigencia = forms.CharField(max_length=100)
    precio = forms.FloatField()