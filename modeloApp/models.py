from django.db import models

# Create your models here.
class Mascotas(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    raza = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50)