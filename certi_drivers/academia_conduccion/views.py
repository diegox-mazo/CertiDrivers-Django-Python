from django.shortcuts import render

# Create your views here.

from academia_conduccion.models import Aprendices, Instructores, Vehiculos, Licencias
from academia_conduccion.forms import *

def create_aprendices(request):

    if request.method == 'GET':
        context = {
            'form': AprendicesForm()
        }
        return render(request, 'aprendices/create_aprendices.html', context=context)

    elif request.method == 'POST':

        form = AprendicesForm(request.POST)
        if form.is_valid():
            Aprendices.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                edad = form.cleaned_data['edad'],
                direccion = form.cleaned_data['direccion'],
                tipo_sangre = form.cleaned_data['tipo_sangre']
            )
            context = {
                'message':'Aprendiz Creado Exitosamente'
            }
            return render(request, 'aprendices/create_aprendices.html', context=context)

        else:
            context = {
                'form_errors': form.errors,
                'form': AprendicesForm()
            }
            return render(request, 'aprendices/create_aprendices.html', context=context)

        # Aprendices.objects.create(nombre = request.POST['nombre'], apellido = request.POST['apellido'], edad = request.POST['edad'], direccion = request.POST['direccion'], tipo_sangre = request.POST['tipo_sangre'])
  

def list_aprendices(request):

    if 'search' in request.GET:
        search = request.GET['search']
        all_aprendices = Aprendices.objects.filter(nombre__icontains = search)

    else:
        all_aprendices = Aprendices.objects.all()

    context = {
        'aprendices': all_aprendices,
    }
    return render(request, 'aprendices/list_aprendices.html', context=context)

##------------------------------------------------------------------------------------------------

def create_instructores(request):

    if request.method == 'GET':
        context = {
            'form': InstructoresForm()
        }
        return render(request, 'instructores/create_instructores.html', context=context)

    elif request.method == 'POST':

        form = InstructoresForm(request.POST)
        if form.is_valid():
            Instructores.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                jornada = form.cleaned_data['jornada'],
            )
            context = {
                'message':'Instructor Creado Exitosamente'
            }
            return render(request, 'instructores/create_instructores.html', context=context)

        else:
            context = {
                'form_errors': form.errors,
                'form': InstructoresForm()
            }
            return render(request, 'instructores/create_instructores.html', context=context)

def list_instructores(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_instructores = Instructores.objects.filter(nombre__icontains = search)

    else:
        all_instructores = Instructores.objects.all()
    context = {
        'instructores': all_instructores,
    }
    return render(request, 'instructores/list_instructores.html', context=context)

##------------------------------------------------------------------------------------------------

def create_vehiculos(request):

    if request.method == 'GET':
        context = {
            'form': VehiculosForm()
        }
        return render(request, 'vehiculos/create_vehiculos.html', context=context)

    elif request.method == 'POST':

        form = VehiculosForm(request.POST)
        if form.is_valid():
            Vehiculos.objects.create(
                tipo = form.cleaned_data['tipo'],
                marca = form.cleaned_data['marca'],
                modelo = form.cleaned_data['modelo'],
                color = form.cleaned_data['color'],
                placa = form.cleaned_data['placa'],
            )
            context = {
                'message':'Vehiculo Creado Exitosamente'
            }
            return render(request, 'vehiculos/create_vehiculos.html', context=context)

        else:
            context = {
                'form_errors': form.errors,
                'form': VehiculosForm()
            }
            return render(request, 'vehiculos/create_vehiculos.html', context=context)

def list_vehiculos(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_vehiculos = Vehiculos.objects.filter(tipo__icontains = search)

    else:
        all_vehiculos = Vehiculos.objects.all()
    context = {
        'vehiculos': all_vehiculos,
    }
    return render(request, 'vehiculos/list_vehiculos.html', context=context)

##------------------------------------------------------------------------------------------------

def create_licencias(request):

    if request.method == 'GET':
        context = {
            'form': LicenciasForm()
        }
        return render(request, 'licencias/create_licencias.html', context=context)

    elif request.method == 'POST':

        form = LicenciasForm(request.POST)
        if form.is_valid():
            Licencias.objects.create(
                clasificacion = form.cleaned_data['clasificacion'],
                descripcion = form.cleaned_data['descripcion'],
                vigencia = form.cleaned_data['vigencia'],
                precio = form.cleaned_data['precio'],
            )
            context = {
                'message':'Licencia Creado Exitosamente'
            }
            return render(request, 'licencias/create_licencias.html', context=context)

        else:
            context = {
                'form_errors': form.errors,
                'form': LicenciasForm()
            }
            return render(request, 'licencias/create_licencias.html', context=context)

def list_licencias(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_licencias = Licencias.objects.filter(clasificacion__icontains = search)

    else:
        all_licencias = Licencias.objects.all()
    context = {
        'licencias': all_licencias,
    }
    return render(request, 'licencias/list_licencias.html', context=context)