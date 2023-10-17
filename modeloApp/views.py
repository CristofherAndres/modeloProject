from django.shortcuts import render
from modeloApp.models import Mascotas

# Create your views here.

def viewMascotas(request):
    # SELECT * FROM MASCOTAS;
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas}

    return render(request, 'modeloApp/viewMascotas.html', data)
