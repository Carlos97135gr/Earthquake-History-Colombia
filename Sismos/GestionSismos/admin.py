from django.contrib import admin
from .models import Departamento,Ciudad,Tipo_Magnitud,Epicentro,Registro_Afectado,Persona
# Register your models here.
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Tipo_Magnitud)
admin.site.register(Epicentro)
admin.site.register(Registro_Afectado)
admin.site.register(Persona )