from django.shortcuts import render

def vista_index(request):
    return render(request, 'index.html', context={})