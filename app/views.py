from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Estudiante
from .forms import EstudianteForm

# Create your views here.
def index(request):
    return render(request,'app/index.html',{'estudiantes': Estudiante.objects.all()})


def views_student(request,id):
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            cod = form.cleaned_data['codigo']
            nom = form.cleaned_data['nombre']
            ape = form.cleaned_data['apellidos']
            edad = form.cleaned_data['edad']
            email = form.cleaned_data['email']
            carrera = form.cleaned_data['carrera']

            obj_estudiante = Estudiante(
                codigo=cod,
                nombre=nom,
                apellidos=ape,
                edad=edad,
                email=email,
                carrera=carrera
            )
            obj_estudiante.save()
            return render(request, 'app/add.html', {'form': EstudianteForm(), 'success': True})
    else:
        form = EstudianteForm()
    return render(request, 'app/add.html', {'form': EstudianteForm()})

def edit(request,id):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(pk=id)
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return render(request, 'app/edit.html', {'form': form, 'success': True})
    else:
        estudiante = Estudiante.objects.get(pk=id)
        form = EstudianteForm(instance=estudiante)
    return render(request, 'app/edit.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(pk=id)
        estudiante.delete()
    return HttpResponseRedirect(reverse('index'))