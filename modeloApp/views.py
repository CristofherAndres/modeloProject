from django.shortcuts import render
from modeloApp.models import Mascotas
from . import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def viewMascotas(request):
    # SELECT * FROM MASCOTAS;
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas}

    return render(request, 'modeloApp/viewMascotas.html', data)

def addMascota(request):

    form = forms.Mascota()

    if request.method == 'POST':
        form = forms.Mascota(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_mascotas'))

    data = {'form': form}
    return render(request, 'modeloApp/formMascota.html',data)

def deleteMascota(request, id):
    """ Buscar la mascota correspondiente con su id """
    mascota = Mascotas.objects.get(id = id)
    mascota.delete()
    return HttpResponseRedirect(reverse('lista_mascotas'))


def editMascota(request, id):
    """ Buscamos la mascota a editar """
    mascota = Mascotas.objects.get(id=id)
    """ Generar formulario con datos de la mascota """
    form = forms.Mascota(instance=mascota)
    if request.method == 'POST':
        form = forms.Mascota(request.POST, instance=mascota)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_mascotas'))
        else:
            print("Errores: ",form.errors)

    data = {'form': form}
    return render(request, 'modeloApp/formMascota.html',data)