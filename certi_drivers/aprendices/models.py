from django.db import models
import datetime

# Create your models here.

class Aprendiz(models.Model):

    blood_choices = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    )
    sex_choices = (
        ('Hombre','Hombre'),
        ('Mujer','Mujer')
    )

    identificacion = models.CharField(max_length=10, unique=True, default=None)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    genero = models.CharField(choices=sex_choices, max_length=10)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    tipo_sangre = models.CharField(choices=blood_choices, max_length=3)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name ='Aprendiz'
        verbose_name_plural = "Aprendices"
