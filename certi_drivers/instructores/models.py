from django.db import models

# Create your models here.

class Instructor(models.Model):

    identificacion = models.CharField(max_length=10, unique=True, default=None)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='instructores', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name ='Instructor'
        verbose_name_plural = "Instructores"
