from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from instructores.models import Instructor
from instructores.forms import InstructoresForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_instructores(request):

    if request.method == 'GET':
        context = {
            'form': InstructoresForm()
        }
        return render(request, 'instructores/create_instructores.html', context=context)

    elif request.method == 'POST':

        form = InstructoresForm(request.POST, request.FILES)
        if form.is_valid():
            Instructor.objects.create(
                identificacion = form.cleaned_data['identificacion'],
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                email = form.cleaned_data['email'],
                telefono = form.cleaned_data['telefono'],
                profile_picture = form.cleaned_data['profile_picture'],
                
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

            

class InstructorDisplayView(ListView):
    model = Instructor
    template_name = 'instructores/display_instructores.html'


class InstructorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Instructor
    template_name = 'instructores/list_instructores.html'

    def test_func(self):
        return self.request.user.is_superuser


class InstructorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Instructor
    template_name = 'instructores/update_instructores.html'
    fields = ('identificacion','nombre', 'apellido','email','telefono','profile_picture')
    success_url = '/instructores/list_instructores'

    def test_func(self):
        return self.request.user.is_superuser


class InstructorDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Instructor
    template_name = 'instructores/delete_instructores.html'
    success_url = '/instructores/list_instructores'

    def test_func(self):
        return self.request.user.is_superuser

