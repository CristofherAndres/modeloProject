from django import forms
from modeloApp.models import Mascotas

class Mascota(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    raza = forms.CharField()
    tipo = forms.CharField()

class MascotaRegistro(forms.ModelForm):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    raza = forms.CharField()
    tipo = forms.CharField()
    class Meta:
        model = Mascotas
        fields = '__all__'