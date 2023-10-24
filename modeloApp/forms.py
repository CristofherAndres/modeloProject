from django import forms
from modeloApp.models import Mascotas
""" Importar libreria para validar datos """
from django.core import validators


class Mascota(forms.Form):
    """ Validar nombre min 5 caracteres """
    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
            validators.MaxLengthValidator(20)]
    )
    edad = forms.IntegerField()
    raza = forms.CharField(required=False)
    tipo = forms.CharField()

    """ Validar la raza de forma personaliza  """
    def clean_raza(self):
        input_raza = self.cleaned_data['raza']
        if input_raza.find('@') == -1:
            raise forms.ValidationError('La raza debe contener al menos 1 @')
        return input_raza

    nombre.widget.attrs['class'] = 'form-control'
    edad.widget.attrs['class'] = 'form-control'
    raza.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'

class Mascota(forms.ModelForm):
    """ Validar nombre min 5 caracteres """
    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
                    validators.MaxLengthValidator(20)]
    )
    edad = forms.IntegerField()
    raza = forms.CharField(required=False)
    tipo = forms.CharField()

    """ Validar la raza de forma personaliza  """
    def clean_raza(self):
        input_raza = self.cleaned_data['raza']
        if input_raza.find('@') == -1:
            raise forms.ValidationError('La raza debe contener al menos 1 @')
        return input_raza

    nombre.widget.attrs['class'] = 'form-control'
    edad.widget.attrs['class'] = 'form-control'
    raza.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mascotas
        fields = '__all__'