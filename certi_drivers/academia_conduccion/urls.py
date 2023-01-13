from django.urls import path
from academia_conduccion.views import create_aprendices, list_aprendices, create_instructores, list_instructores, create_vehiculos, list_vehiculos, create_licencias, list_licencias

urlpatterns = [
    path('create_aprendices/', create_aprendices, name='create_aprendices'),
    path('list_aprendices/', list_aprendices, name='list_aprendices'),

    path('create_instructores/', create_instructores, name='create_instructores'),
    path('list_instructores/', list_instructores, name='list_instructores'),

    path('create_vehiculos/', create_vehiculos, name='create_vehiculos'),
    path('list_vehiculos/', list_vehiculos, name='list_vehiculos'),

    path('create_licencias/', create_licencias, name='create_licencias'),
    path('list_licencias/', list_licencias, name='list_licencias'),
]