from django.contrib import admin
from .models import Evento
#para ver los permisos en el admin
from django.contrib.auth.models import Permission


# Register your models here.
admin.site.register(Evento)
admin.site.register(Permission)


