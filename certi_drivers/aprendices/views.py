from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from aprendices.models import Aprendiz
from aprendices.forms import AprendicesForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_aprendices(request):

    if request.method == 'GET':
        context = {
            'form': AprendicesForm()
        }
        return render(request, 'aprendices/create_aprendices.html', context=context)

    elif request.method == 'POST':

        form = AprendicesForm(request.POST)
        if form.is_valid():
            Aprendiz.objects.create(
                identificacion = form.cleaned_data['identificacion'],
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                email = form.cleaned_data['email'],
                genero = form.cleaned_data['genero'],
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


def list_aprendices(request):

    if 'search' in request.GET:
        search = request.GET['search']
        all_aprendices = Aprendiz.objects.filter(nombre__icontains = search, is_active = True)

    else:
        all_aprendices = Aprendiz.objects.filter(is_active = True)

    context = {
        'aprendices': all_aprendices,
    }
    return render(request, 'aprendices/list_aprendices.html', context=context)


class AprendizListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Aprendiz
    template_name = 'aprendices/list_aprendices.html'

    def test_func(self):
        return self.request.user.is_superuser


class AprndizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Aprendiz
    template_name = 'aprendices/update_aprendices.html'
    fields = ('identificacion','nombre', 'apellido','email','genero','edad','direccion','tipo_sangre')
    success_url = '/aprendices/list_aprendices'

    def test_func(self):
        return self.request.user.is_superuser


class AprendizDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Aprendiz
    template_name = 'aprendices/delete_aprendices.html'
    success_url = '/aprendices/list_aprendices'

    def test_func(self):
        return self.request.user.is_superuser



