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
        form = forms.MascotaRegistro(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_mascotas'))

    data = {'form': form}
    return render(request, 'modeloApp/formMascota.html',data)
