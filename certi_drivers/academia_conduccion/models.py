from django.db import models

# Create your models here.

class Aprendices(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    tipo_sangre = models.CharField(max_length=3)


class Instructores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    jornada = models.CharField(max_length=50)


class Vehiculos(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)


class Licencias(models.Model):
    clasificacion = models.CharField(max_length=2, unique=True)
    descripcion = models.CharField(max_length=100)
    vigencia = models.CharField(max_length=100)
    precio = models.FloatField()
    