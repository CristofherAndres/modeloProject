from django.contrib import admin

# Register your models here.
from modeloApp.models import Mascotas


class MascotaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','edad','raza','tipo']


admin.site.register(Mascotas, MascotaAdmin)