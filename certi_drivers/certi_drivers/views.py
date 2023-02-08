from django.shortcuts import render

def vista_index(request):
    return render(request, 'index.html', context={})

def vista_about(request):
    return render(request, 'about.html', context={})

def vista_licencias(request):
    return render(request, 'licencias/display_licencias.html', context={})